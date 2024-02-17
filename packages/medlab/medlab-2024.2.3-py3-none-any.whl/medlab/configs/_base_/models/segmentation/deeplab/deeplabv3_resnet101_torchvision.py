model = dict(
    type='deeplabv3_resnet101_torchvision',
    progress=True,
    aux_loss=False,
    num_classes=1,
    # weights=None,
    weights_backbone=None
)
