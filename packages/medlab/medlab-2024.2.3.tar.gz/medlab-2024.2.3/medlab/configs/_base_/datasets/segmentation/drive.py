# 分割任务BaseSegDataset
dataset_type = 'BaseSegDataset'

# 数据集的根目录
data_root = 'data/DRIVE'

in_channels = 3  # 数据集的图片通道数, 彩色为3, 灰度为1
num_classes = 1  # 分割类别, 对于单目标分割, 填1时后续训练中处理会使用sigmoid, 填2时后续处理会使用softmax

# 非必填项目, 用于指定后面数据增强和滑动窗口推理时的图片大小
crop_size = (128, 128)

# 训练数据增强, 接口详情见MONAI官网, type指定数据增强类型, keys指定增强用于images、labels或both, 不要改变images、labels名称
# 如果使用了类似RandCropByPosNegLabeld这类裁剪返回多个数据的transform，实际训练时的batch_size = num_samples*batch_size
# 注意检查数据增强后的images和labels的shape和value时候符合预期
train_transform = [  # LoadImaged的reader参数一般不用指定, 在数据无法正确加载时, 需要调试找到指定的Reader或自定义Reader
    dict(type='LoadImaged', keys=['images', 'labels'], reader='PILReader', ensure_channel_first=True, image_only=True),
    dict(type='ScaleIntensityd', keys=['images', 'labels']),
    dict(type='RandZoomd', keys=['images', 'labels'], prob=0.5, min_zoom=0.8, max_zoom=1.2,
         mode=("bilinear", "nearest")),
    dict(type='RandRotated', keys=['images', 'labels'], prob=0.5, range_x=0.3, mode=("bilinear", "nearest")),
    dict(type='RandAxisFlipd', keys=['images', 'labels'], prob=0.5),
    dict(type='RandCropByPosNegLabeld', keys=['images', 'labels'], label_key='labels', spatial_size=crop_size, pos=1,
         neg=1, num_samples=4, image_key='images', image_threshold=0, ),
    dict(type='RandShiftIntensityd', keys=['images'], offsets=0.10, prob=0.50)]

val_transform = [dict(type='LoadImaged', keys=['images', 'labels'], reader='PILReader', ensure_channel_first=True),
                 dict(type='ScaleIntensityd', keys=['images', 'labels'])]

train_dataloader = dict(batch_size=4,  # 实际为batch_size*num_samples=4*4=16
                        num_workers=0,
                        dataset=dict(type=dataset_type, img_suffix='_training.tif', label_suffix='_manual1.gif',
                                     data_root=data_root,
                                     img_dir='training/images', label_dir='training/1st_manual', subset='train',
                                     test_size=0.2, seed=1234,
                                     transforms=train_transform))

val_dataloader = dict(batch_size=1,  # 为了避免测试图片大小不等、可视化等因素，建议设为1
                      num_workers=0,
                      dataset=dict(type=dataset_type, img_suffix='_training.tif', label_suffix='_manual1.gif',
                                   data_root=data_root,
                                   img_dir='training/images', label_dir='training/1st_manual', subset='val',
                                   test_size=0.2, seed=1234,
                                   transforms=val_transform))

test_dataloader = val_dataloader

# 验证\测试时的推理模式, SimpleInferer直接推理整张图, SlidingWindowInferer为滑动窗口推理, 接口详情见MONAI官网
# inferer=dict(type='SimpleInferer')
inferer = dict(type='SlidingWindowInferer', roi_size=crop_size, sw_batch_size=4)

train_cfg = dict()  # 训练时的配置
val_cfg = dict(inferer=inferer)  # 验证时的配置
test_cfg = dict(inferer=inferer, output_ext='.png', scale=255)  # output_ext测试保存预测图片时的后缀
# scale保存预测的图片是否需要将像素值缩放, 单目标分割可填，多目标不建议填写该参数
