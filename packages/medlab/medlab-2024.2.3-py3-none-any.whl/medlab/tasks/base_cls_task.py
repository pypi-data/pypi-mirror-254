from typing import Any
from monai.data import decollate_batch
from monai.utils.enums import PostFix

from medlab.registry import TASKS, INFERERS, TRANSFORMS
from .base_task import BaseTask
import torch
import copy
from monai.metrics import ConfusionMatrixMetric
from sklearn.metrics import roc_curve, auc, RocCurveDisplay, confusion_matrix, ConfusionMatrixDisplay
import pathlib
import pandas as pd
import os
import numpy as np
from itertools import cycle
import matplotlib.pyplot as plt
import json
from copy import deepcopy


@TASKS.register_module()
class BaseClsTask(BaseTask):
    def __init__(self, *args, **kwargs):
        """
        base classification task, one input, one output
        """
        super().__init__(*args, **kwargs)
        self.val_inferer = INFERERS.build(self.val_cfg.get('inferer', dict(type='SimpleInferer')))
        self.test_inferer = INFERERS.build(self.test_cfg.get('inferer', dict(type='SimpleInferer')))
        num_classes = kwargs.get('num_classes', None)
        assert num_classes is not None, "num_classes must be specified in model"
        if num_classes == 1:
            self.post_pred_act = TRANSFORMS.build([
                dict(type='ToDevice', device='cpu'),
                dict(type='Activations', sigmoid=True)
            ])
            self.post_pred_cls = TRANSFORMS.build([
                dict(type='AsDiscrete', threshold=0.5)
            ])
            self.post_label = TRANSFORMS.build([dict(type='ToDevice', device='cpu')])

            post_save = []
        else:
            self.post_pred_act = TRANSFORMS.build([
                dict(type='ToDevice', device='cpu'),
                dict(type='Activations', softmax=True)
            ])

            self.post_pred_cls = TRANSFORMS.build([
                dict(type='AsDiscrete', argmax=True, to_onehot=num_classes),
            ])
            self.post_label = TRANSFORMS.build([
                dict(type='AsDiscrete', to_onehot=num_classes),
                dict(type='ToDevice', device='cpu')
            ])
            post_save = [
                dict(type='AsDiscreted', keys='preds', argmax=True)
            ]
        save_dir = self.test_cfg.get('save_dir', None)
        if save_dir is not None:
            post_save.extend([
                dict(
                    type='CopyItemsd',
                    keys=PostFix.meta("images"),
                    times=1,
                    names=PostFix.meta("preds")
                ),
                dict(
                    type='SaveClassificationd',
                    keys='preds',
                    saver=None,
                    meta_keys=None,
                    output_dir=save_dir,
                    filename='predictions.csv',
                    delimiter=",",
                    overwrite=True)
            ])
        self.post_save = TRANSFORMS.build(post_save)

        self.train_metrics_key = copy.deepcopy(self.metrics_key)
        self.train_metrics = copy.deepcopy(self.metrics)

        self.val_metrics_key = copy.deepcopy(self.metrics_key)
        self.val_metrics = copy.deepcopy(self.metrics)

        if 'ROCAUCMetric' in self.metrics_key:
            index_train = self.train_metrics_key.index('ROCAUCMetric')
            index_val = self.train_metrics_key.index('ROCAUCMetric')
            self.train_metrics_key.pop(index_train)
            self.val_metrics_key.pop(index_val)
            self.train_roc_auc_metric = self.train_metrics.pop(index_train)
            self.val_roc_auc_metric = self.val_metrics.pop(index_val)
        else:
            self.train_roc_auc_metric = None
            self.val_roc_auc_metric = None

        self.training_step_loss = []
        self.validation_step_loss = []
        self.test_names = []
        self.test_labels = []
        self.test_preds = []

    def forward(self, x):
        return self._model(x)

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


        loss = self.loss_func(outputs, labels)

        if isinstance(outputs, (tuple, list)):
            outputs = outputs[0]

        outputs = [self.post_pred_act(i) for i in decollate_batch(outputs)]
        labels = [self.post_label(i) for i in decollate_batch(labels)]

        if self.train_roc_auc_metric is not None:
            self.train_roc_auc_metric(outputs, labels)
        
        outputs = [self.post_pred_cls(i) for i in outputs]

        if len(self.train_metrics) > 0:
            for metric in self.train_metrics:
                metric(outputs, labels)

        self.training_step_loss.append(loss)

        # self.log("train_step_loss", loss.item(), sync_dist=True, batch_size=batch_size)
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
        outputs = self.val_inferer(inputs=images, network=self.forward)

        loss = self.loss_func(outputs, labels)


        if isinstance(outputs, (tuple, list)):
            outputs = outputs[0]

        outputs = [self.post_pred_act(i) for i in decollate_batch(outputs)]
        labels = [self.post_label(i) for i in decollate_batch(labels, detach=False)]

        if self.val_roc_auc_metric is not None:
            self.val_roc_auc_metric(outputs, labels)

        outputs = [self.post_pred_cls(i) for i in outputs]

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


    def test_step(self, batch, batch_idx):
        """
        test step for classification task, save predictions to csv file
        :param batch: batch data
        :param batch_idx: batch index
        :return:
        """
 
        images = batch["images"]
        labels = batch["labels"]

        outputs = self.test_inferer(inputs=images, network=self.forward)

        if isinstance(outputs, (tuple, list)):
            outputs = outputs[0]

        batch["preds"] = outputs

        outputs = [self.post_pred_act(i) for i in decollate_batch(outputs)]
        labels = [self.post_label(i) for i in decollate_batch(labels)]

        if self.val_roc_auc_metric is not None:
            self.val_roc_auc_metric(outputs, labels)

        outputs = [self.post_pred_cls(i) for i in outputs]

        if len(self.val_metrics) > 0:
            for metric in self.val_metrics:
                metric(outputs, labels)

        for i in decollate_batch(batch):
            # self.post_save(i)
            filename = i['images_meta_dict']['filename_or_obj']
            # filename = pathlib.Path(filename).name
            self.test_names.append(filename)
            self.test_labels.append(i['labels'])
            self.test_preds.append(torch.argmax(i['preds']).item())

        self.log("test_step", batch_idx, sync_dist=True, batch_size=images.shape[0])

    def on_test_epoch_end(self):
        """
        test epoch end hook, parse metrics
        """
    
        df = pd.DataFrame({'name': self.test_names, 'label': self.test_labels, 'pred': self.test_preds})
        df.to_csv(os.path.join(self.test_cfg.get('save_dir'), "test.csv"), index=False)

        if self.val_roc_auc_metric is not None:
            y_pred_prob, y = self.val_roc_auc_metric.get_buffer()
            y_pred = torch.argmax(y_pred_prob, dim=1, keepdim=True)
            y_pred_ont_hot = torch.zeros_like(y_pred_prob)
            y_pred_ont_hot.scatter_(1, y_pred, 1)

            meta = self._test_dataloader.dataset.META_INFO['classes']
            target_names = [meta[i] for i in sorted(meta.keys())]
            num_classes = len(target_names)

            # 绘制混淆矩阵
            # 分别设置图片大小和画布大小，保证图片中的内容不被截断
            fig, ax = plt.subplots(figsize=(8, 6))
            cmap = plt.cm.Blues
            cm = confusion_matrix(torch.argmax(y, dim=1).cpu().numpy().ravel(), y_pred.cpu().numpy().ravel())
            disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
            disp.plot(include_values=True, cmap=cmap, ax=ax, xticks_rotation='horizontal')
            ax.set_title("Confusion Matrix")
            plt.savefig(os.path.join(self.test_cfg.get('save_dir'), "confusion_matrix.png"))


            cfm = ConfusionMatrixMetric(
                metric_name=("accuracy", "sensitivity", "specificity", "precision", "recall", "f1_score")
            )
            cfm(y_pred_ont_hot, y)

            acc, sen, spe, pre, rec, f1 = [i.item() for i in cfm.aggregate()]
            test_rst = {}
            test_rst['accuracy'] = acc
            test_rst['sensitivity'] = sen
            test_rst['specificity'] = spe
            test_rst['precision'] = pre
            test_rst['recall'] = rec
            test_rst['f1_score'] = f1

            df[df["pred"] != df["label"]].to_csv(os.path.join(self.test_cfg.get('save_dir'), "error.csv"), index=False)
            json.dump(test_rst, open(os.path.join(self.test_cfg.get('save_dir'), "metric.json"), 'w'), indent=4)
            
            
            y_pred_prob = y_pred_prob.cpu().numpy()
            y = y.cpu().numpy()

            if num_classes == 2:
                y = y[:, 1].ravel()
                y_pred_prob = y_pred_prob[:, 1].ravel()
                fpr, tpr, thresholds = roc_curve(y, y_pred_prob)
                roc_auc = auc(fpr, tpr)
                fig, ax = plt.subplots(figsize=(6, 6))
                RocCurveDisplay.from_predictions(
                    y,
                    y_pred_prob,
                    name=f"ROC curve for {target_names[1]}",
                    color="deeppink",
                    ax=ax
                )
                plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
                _ = ax.set(
                    xlabel="False Positive Rate",
                    ylabel="True Positive Rate",
                    title="Receiver Operating Characteristic",
                )
                ax.set_xlim([-0.01, 1.01])
                ax.set_ylim([-0.01, 1.01])
                fig.savefig(os.path.join(self.test_cfg.get('save_dir'), "roc.png"))
            else:
                fpr, tpr, roc_auc = dict(), dict(), dict()
                fpr["micro"], tpr["micro"], _ = roc_curve(y.ravel(), y_pred_prob.ravel())
                roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

                for i in range(num_classes):
                    fpr[i], tpr[i], _ = roc_curve(y[:, i], y_pred_prob[:, i])
                    roc_auc[i] = auc(fpr[i], tpr[i])
                fpr_grid = np.linspace(0.0, 1.0, 1000)
                mean_tpr = np.zeros_like(fpr_grid)
                for i in range(num_classes):
                    mean_tpr += np.interp(fpr_grid, fpr[i], tpr[i])  # linear interpolation
                mean_tpr /= num_classes

                fpr["macro"] = fpr_grid
                tpr["macro"] = mean_tpr
                roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
                fig, ax = plt.subplots(figsize=(6, 6))

                plt.plot(
                    fpr["micro"],
                    tpr["micro"],
                    label=f"micro-average ROC curve (AUC = {roc_auc['micro']:.2f})",
                    color="deeppink",
                    linestyle=":",
                    linewidth=4,
                )

                plt.plot(
                    fpr["macro"],
                    tpr["macro"],
                    label=f"macro-average ROC curve (AUC = {roc_auc['macro']:.2f})",
                    color="navy",
                    linestyle=":",
                    linewidth=4,
                )

                colors = cycle(["aqua", "darkorange", "cornflowerblue"])
                
                for class_id, color in zip(range(num_classes), colors):
                    RocCurveDisplay.from_predictions(
                        y[:, class_id],
                        y_pred_prob[:, class_id],
                        name=f"ROC curve for {target_names[class_id]}",
                        color=color,
                        ax=ax
                        # plot_chance_level=(class_id == 2),
                    )

                plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
                
                _ = ax.set(
                xlabel="False Positive Rate",
                ylabel="True Positive Rate",
                title="Extension of Receiver Operating Characteristic\nto One-vs-Rest multiclass",
                )
                

                ax.set_xlim([-0.01, 1.01])
                ax.set_ylim([-0.01, 1.01])

                fig.savefig(os.path.join(self.test_cfg.get('save_dir'), "roc.png"))
       
       
        

    def predict_step(self, batch, batch_idx, dataloader_idx=0) -> Any:
        images = batch["images"]
        outputs = self.test_inferer(inputs=images, network=self.forward)
        if isinstance(outputs, (tuple, list)):
            outputs = outputs[0]
        batch["preds"] = outputs
        for i in decollate_batch(batch):
            self.test_names.append(i['images_meta_dict']['filename_or_obj'])
            self.test_preds.append(torch.argmax(i['preds']).item())


    def on_predict_epoch_end(self):
        df = pd.DataFrame({'name': self.test_names, 'pred': self.test_preds})
        df.to_csv(os.path.join(self.test_cfg.get('save_dir'), "predictions.csv"), index=False, encoding='utf-8')

    def parse_train_metrics(self):
        """
        parse metrics to dict
        :return: metrics dict
        """
        value_dict = {}
        values = []
        if self.train_roc_auc_metric is not None:
            value_dict['ROCAUCMetric'] = self.train_roc_auc_metric.aggregate()
            self.train_roc_auc_metric.reset()

        for metric in self.train_metrics:
            value = metric.aggregate()

            if isinstance(value, list):
                values.extend([v.item() for v in value])
            else:
                values.append(value.item())
        value_dict.update(dict(zip(self.train_metrics_key, values)))

        for metric in self.metrics:
            metric.reset()
        
        value_dict = {f'train_{k}': v for k, v in value_dict.items()}

        return value_dict

    def parse_val_metrics(self):
        """
        parse metrics to dict
        :return: metrics dict
        """
        value_dict = {}
        values = []
        if self.val_roc_auc_metric is not None:
            value_dict['ROCAUCMetric'] = self.val_roc_auc_metric.aggregate()
            self.val_roc_auc_metric.reset()

        for metric in self.val_metrics:
            value = metric.aggregate()

            if isinstance(value, list):
                values.extend([v.item() for v in value])
            else:
                values.append(value.item())
        value_dict.update(dict(zip(self.val_metrics_key, values)))

        for metric in self.metrics:
            metric.reset()
        
        value_dict = {f'val_{k}': v for k, v in value_dict.items()}

        return value_dict