model = dict(
    type='vnet_monai',
    spatial_dims=3,
    in_channels=1,
    out_channels=1,
    act=("elu", {"inplace": True}),
    dropout_prob=0.5,
    bias=False
)
