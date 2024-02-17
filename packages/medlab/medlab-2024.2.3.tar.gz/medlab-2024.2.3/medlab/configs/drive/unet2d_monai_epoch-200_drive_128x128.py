_base_ = [
    '../_base_/models/segmentation/unet/unet2d_monai.py',
    '../_base_/datasets/segmentation/drive.py',
    '../_base_/schedules/seg_epoch_schedule.py'
]

in_channels = {{_base_.in_channels}}
num_classes = {{_base_.num_classes}}

model = dict(in_channels=in_channels, out_channels=num_classes)

loss_func = dict(type='DiceCELoss', sigmoid=True)
trainer = dict(max_epochs=200, check_val_every_n_epoch=1)
