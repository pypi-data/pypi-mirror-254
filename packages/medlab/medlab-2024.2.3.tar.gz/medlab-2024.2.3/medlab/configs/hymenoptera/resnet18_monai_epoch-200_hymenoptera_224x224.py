_base_ = ['../_base_/models/classification/resnet/resnet18_monai.py',
          '../_base_/datasets/classification/hymenoptera.py', '../_base_/schedules/cls_epoch_schedule.py']

in_channels = {{_base_.in_channels}}
num_classes = {{_base_.num_classes}}

model = dict(n_input_channels=in_channels, num_classes=num_classes, pretrained=False)

loss_func = dict(type='CrossEntropyLoss')
trainer = dict(max_epochs=20, check_val_every_n_epoch=1)
