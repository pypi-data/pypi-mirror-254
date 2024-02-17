model = dict(
    type='deeplabv3_mobilenet_v3_large_torchvision',
    progress=True,
    aux_loss=False,
    num_classes=1,
    # weights=None,
    weights_backbone=None
)
