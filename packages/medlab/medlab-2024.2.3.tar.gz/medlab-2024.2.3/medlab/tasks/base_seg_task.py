import os.path as osp

from monai.data import decollate_batch

from medlab.registry import TASKS, INFERERS, TRANSFORMS
from .base_task import BaseTask
from typing import Any, OrderedDict, Dict
import copy
import torch
import pandas as pd
import os
import json
import pathlib
from copy import deepcopy
@TASKS.register_module()
class BaseSegTask(BaseTask):
    def __init__(self, *args, **kwargs):
        """
        base segmentation task, one input, one output
        """
        super().__init__(*args, **kwargs)
        self.val_inferer = INFERERS.build(self.val_cfg.get('inferer', dict(type='SimpleInferer')))
        self.test_inferer = INFERERS.build(self.test_cfg.get('inferer', dict(type='SimpleInferer')))
        num_classes = kwargs.get('num_classes', None)
        assert num_classes is not None, "num_classes must be specified in model"
        if num_classes == 1:
            self.post_pred = TRANSFORMS.build([
                dict(type='Activations', sigmoid=True),
                dict(type='AsDiscrete', threshold=0.5)
            ])
            self.post_label = TRANSFORMS.build([])
            post_save = [
                dict(type='ToDevice', device='cpu'),
            ]
        else:
            self.post_pred = TRANSFORMS.build([dict(type='AsDiscrete', argmax=True, to_onehot=num_classes)])
            self.post_label = TRANSFORMS.build([dict(type='AsDiscrete', to_onehot=num_classes)])
            post_save = [
                dict(type='AsDiscrete', argmax=True),
                dict(type='ToDevice', device='cpu')
            ]
        save_dir = self.test_cfg.get('save_dir', None)
        pred_save = None
        if save_dir is not None:
            post_save.append(
                dict(
                    type='SaveImage',
                    output_dir=osp.join(self.test_cfg.get('save_dir', None), 'test_result'),
                    resample=True,
                    output_postfix='',
                    output_ext=self.test_cfg.get('output_ext', '.png'),
                    scale=self.test_cfg.get('scale', 255.0),
                    squeeze_end_dims=True,
                    separate_folder=False
                )
            )
            pred_save = deepcopy(post_save)
            pred_save[-1]['output_dir'] = osp.join(self.test_cfg.get('save_dir', None), 'predict_result')

        self.post_save = TRANSFORMS.build(post_save) if post_save is not None else None
        self.pred_save = TRANSFORMS.build(pred_save) if pred_save is not None else None
        self.train_metrics_key = copy.deepcopy(self.metrics_key)
        self.train_metrics = copy.deepcopy(self.metrics)

        self.val_metrics_key = copy.deepcopy(self.metrics_key)
        self.val_metrics = copy.deepcopy(self.metrics)

        self.training_step_loss = []
        self.validation_step_loss = []

        self.test_names = []
        self.test_dice = []
        self.test_acc = []

    def forward(self, x):
        return self.parse_outputs(self._model(x))

    def training_step(self, batch, batch_idx):
        """
        training step for classification task
        :param batch: batch data
        :param batch_idx: batch index
        :return: loss
        """
        images = batch['images']
        labels = batch['labels']

        batch_size = images.shape[0]
        outputs = self.forward(images)
        
        if self.loss_func.__class__.__name__ == 'CrossEntropyLoss':
            labels = labels.squeeze(1).long()
        loss = self.loss_func(outputs, labels)

        if self.loss_func.__class__.__name__ == 'CrossEntropyLoss':
            labels = labels.unsqueeze(1).long()

        if isinstance(outputs, (tuple, list)):
            outputs = outputs[0]

        outputs = [self.post_pred(i) for i in decollate_batch(outputs)]
        labels = [self.post_label(i) for i in decollate_batch(labels)]


        if len(self.train_metrics) > 0:
            for metric in self.train_metrics:
                metric(outputs, labels)
        
        self.training_step_loss.append(loss)
        # self.log("train_step_loss", loss, sync_dist=True, batch_size=batch_size)
        
        
        return loss

    def on_train_epoch_end(self):
        self.log_dict(self.parse_train_metrics(), sync_dist=True)
        epoch_mean = torch.stack(self.training_step_loss).mean()
        self.log("train_loss", epoch_mean.item(), sync_dist=True)
        self.training_step_loss.clear()

    def validation_step(self, batch, batch_idx):
        """
        validation step for classification task
        :param batch: batch data
        :param batch_idx: batch index
        :return: None
        """
        images = batch['images']
        labels = batch['labels']

        batch_size = images.shape[0]
        # outputs = self.forward(images)
        outputs = self.val_inferer(inputs=images, network=self.forward)

        if self.loss_func.__class__.__name__ == 'CrossEntropyLoss':
            labels = labels.squeeze(1).long()
        loss = self.loss_func(outputs, labels)
        if self.loss_func.__class__.__name__ == 'CrossEntropyLoss':
            labels = labels.unsqueeze(1).long()

        if isinstance(outputs, (tuple, list)):
            outputs = outputs[0]

        outputs = [self.post_pred(i) for i in decollate_batch(outputs)]
        labels = [self.post_label(i) for i in decollate_batch(labels)]

        if len(self.val_metrics) > 0:
            for metric in self.val_metrics:
                metric(outputs, labels)
        self.validation_step_loss.append(loss)

        # self.log('val_step_loss', loss.item(), sync_dist=True, batch_size=batch_size)

    def on_validation_epoch_end(self):
        """
        validation epoch end hook, parse and log metrics
        """
        self.log_dict(self.parse_val_metrics(), sync_dist=True)
        epoch_mean = torch.stack(self.validation_step_loss).mean()
        self.log("val_loss", epoch_mean.item(), sync_dist=True)
        self.validation_step_loss.clear()
        # self.log_dict(self.parse_metrics(), sync_dist=True)

    def test_step(self, batch, batch_idx):
        """
        test step for classification task, save predictions to disk
        :param batch: batch data
        :param batch_idx: batch index
        :return:
        """
        images = batch["images"]
        labels = batch["labels"]

        outputs = self.test_inferer(inputs=images, network=self.forward)

        if isinstance(outputs, (tuple, list)):
            outputs = outputs[0]

        outputs = [self.post_pred(i) for i in decollate_batch(outputs)]
        labels = [self.post_label(i) for i in decollate_batch(labels)]

        for metric in self.metrics:
            metric(outputs, labels)

        if len(self.val_metrics) > 0:
            for metric in self.val_metrics:
                metric(outputs, labels)

        # outputs[0].meta['filename_or_obj'] = batch['images_meta_dict']['filename_or_obj'][0]

        # print(self.post_save(outputs[0]))
        for i in outputs:
            self.post_save(i)
            self.test_names.append(i.meta['filename_or_obj'])


    def on_test_epoch_end(self):
        """
        test epoch end hook, parse metrics
        """
        for i in self.val_metrics:
            if i.__class__.__name__ == "DiceMetric":
                # 展开成一维
                i.reduction = "none"
                self.test_dice = i.aggregate().cpu().numpy().ravel().tolist()
                
            if i.__class__.__name__ == "ConfusionMatrixMetric":
                i.reduction = "none"
                self.test_acc = i.aggregate()[0].cpu().numpy().ravel().tolist()
        
        df = pd.DataFrame({'name': self.test_names, 'dice': self.test_dice, 'accuracy': self.test_acc})
        file_path = pathlib.Path(df['name'][0])
        base_dir = file_path.parent.parent
        df['label'] = [os.path.join(base_dir, 'Segmentation', pathlib.Path(i).name) for i in df['name']]
        save_dir = self.test_cfg.get('save_dir', None)
        df['pred'] = [os.path.join(save_dir, 'test_result', pathlib.Path(i).name) for i in df['name']]
        
        df.to_csv(os.path.join(save_dir, "test.csv"), index=False, encoding='utf-8')
        dice = df['dice'].mean()
        acc = df['accuracy'].mean()
        metric = {'dice': dice, 'accuracy': acc}
        json_path = os.path.join(save_dir, "metric.json")
        with open(json_path, 'w') as f:
            json.dump(metric, f)

    def parse_train_metrics(self):
        """
        parse metrics to dict
        :return: metrics dict
        """
        values = []
        for metric in self.train_metrics:
            value = metric.aggregate()

            if isinstance(value, list):
                values.extend([v.item() for v in value])
            else:
                values.append(value.item())

        value_dict = dict(zip(self.train_metrics_key, values))
        for metric in self.train_metrics:
            metric.reset()
        value_dict = {f'train_{k}': v for k, v in value_dict.items()}
        return value_dict

    def predict_step(self, batch, batch_idx, dataloader_idx=0) -> Any:
        images = batch["images"]
        outputs = self.test_inferer(inputs=images, network=self.forward)
        if isinstance(outputs, (tuple, list)):
            outputs = outputs[0]
        outputs = [self.post_pred(i) for i in decollate_batch(outputs)]
        batch["preds"] = outputs
        
        for i in outputs:
            self.pred_save(i)

    def parse_val_metrics(self):
        """
        parse metrics to dict
        :return: metrics dict
        """
        values = []
        for metric in self.val_metrics:
            value = metric.aggregate()

            if isinstance(value, list):
                values.extend([v.item() for v in value])
            else:
                values.append(value.item())

        value_dict = dict(zip(self.val_metrics_key, values))
        for metric in self.val_metrics:
            metric.reset()
        value_dict = {f'val_{k}': v for k, v in value_dict.items()}
        return value_dict

    @staticmethod
    def parse_outputs(outputs):
        """
        parse outputs to tensor or list
        :return: outputs dict
        """
        if isinstance(outputs, (OrderedDict, Dict)):
            outputs = list(outputs.values())
            if len(outputs) == 1:
                outputs = outputs[0]
        return outputs
