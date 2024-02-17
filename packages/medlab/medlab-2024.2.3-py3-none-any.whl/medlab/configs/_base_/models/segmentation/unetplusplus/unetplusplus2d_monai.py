model = dict(
    type='unetplusplus_monai',
    spatial_dims=2,
    in_channels=1,
    out_channels=2,
    features=(32, 32, 64, 128, 256, 32),
    deep_supervision=False,
    act=("LeakyReLU", {"negative_slope": 0.1, "inplace": True}),
    norm=("instance", {"affine": True}),
    bias=True,
    dropout=0.0, upsample="deconv")
