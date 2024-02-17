model = dict(
    type='attentionunet_monai',
    spatial_dims=3,
    in_channels=1,
    out_channels=1,
    channels=(16, 32, 64, 128, 256),
    strides=(2, 2, 2, 2),
    kernel_size=3,
    up_kernel_size=3,
    dropout=0.0,
)
