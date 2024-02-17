model = dict(
    type='swinunetr_monai',
    img_size=(96, 96, 96),
    in_channels=3,
    out_channels=1,
    depths=(2, 2, 2, 2),
    num_heads=(3, 6, 12, 24),
    feature_size=24,
    norm_name="instance",
    drop_rate=0.0,
    attn_drop_rate=0.0,
    dropout_path_rate=0.0,
    normalize=True,
    use_checkpoint=False,
    spatial_dims=3,
    downsample="merging"
)
