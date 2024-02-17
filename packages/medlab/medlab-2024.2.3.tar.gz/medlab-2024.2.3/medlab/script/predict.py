import argparse
import logging
import os.path as osp
import warnings
import os
from monai.data import DataLoader, Dataset

from lightning.pytorch import seed_everything
from mmengine.config import Config

from medlab.registry import TRAINERS, TASKS, TRANSFORMS


def parse_args():
    parser = argparse.ArgumentParser(description='Train a segmentor')
    parser.add_argument('checkpoint', help='model checkpoint file path')
    parser.add_argument('path', help='predict file or dir path of filelist')
    parser.add_argument('--save-dir', help='the dir to save logs and models')
    args = parser.parse_args()
    return args

def get_predict_files(path):
    try:
        path = eval(path)
    except:
        path = str(path)
        

    files = []
    if isinstance(path, list):
        files = path
    else:
        if os.path.isdir(path):
            for file in os.listdir(path):
                filename = os.path.join(path, file)
                if os.path.isfile(filename):
                    files.append(filename)
        if os.path.isfile(path):
            files.append(path)
    files = sorted(files)
    files = [{'images': i} for i in files]
    return files


def predict():
    warnings.filterwarnings("ignore")
    logging.disable(logging.WARNING)
    args = parse_args()
    assert args.path
    cfg_path = osp.join(osp.dirname(osp.dirname(args.checkpoint)), 'config.py')

    assert osp.exists(cfg_path)

    cfg = Config.fromfile(cfg_path)

    seed = cfg.get('seed', 1)
    ckpt_path = cfg.get('ckpt_path', None)
    trainer_cfg = cfg.get('trainer', dict())
    seed_everything(seed)
    
    if args.checkpoint is not None:
        ckpt_path = args.checkpoint

    if args.save_dir is not None:
        # update configs according to CLI args if args.work_dir is not None
        save_dir = args.save_dir
    else:
        save_dir = cfg.get('save_dir', osp.join(osp.dirname(ckpt_path), osp.splitext(osp.basename(ckpt_path))[0]))

    trainer_cfg['default_root_dir'] = save_dir

    trainer = TRAINERS.build(trainer_cfg)

    test_cfg = cfg.get('test_cfg', dict())
    test_cfg.update(dict(save_dir=save_dir))

    
    files = get_predict_files(args.path)
    predict_transforms = cfg.val_dataloader.dataset.transforms
    new_transforms = []
    for d in predict_transforms:
        for key in ['keys', 'mode']:
            if key in d and isinstance(d[key], list):
                d[key] = d[key][0]
        if d['keys'] == 'labels':
            continue
        new_transforms.append(d)
    print(new_transforms)
    new_transforms = TRANSFORMS.build(new_transforms)
    predict_dataset = Dataset(data=files, transform=new_transforms)
    predict_dataloader = DataLoader(dataset=predict_dataset, batch_size=1, num_workers=0)


    task = TASKS.build(
        dict(
            type=cfg.get('task_type', None),
            model=cfg.get('model', None),
            train_dataloader=None,
            val_dataloader=None,
            test_dataloader=None,
            loss_func=cfg.get('loss_func', None),
            optims=None,
            metrics=cfg.get('metrics', None),
            train_cfg=dict(),
            val_cfg=dict(),
            test_cfg=test_cfg,
            num_classes=cfg.get('num_classes', None)
        )
    )
    trainer.predict(task, dataloaders=predict_dataloader, ckpt_path=ckpt_path)


if __name__ == '__main__':
    predict()
