model = dict(
    type='fcn_resnet50_torchvision',
    progress=True,
    aux_loss=False,
    num_classes=1,
    weights=None,
    weights_backbone=None
)
