# 分类任务BaseSegDataset
dataset_type = 'BaseClsDataset'

# 数据集的根目录
data_root = 'E:/dataset/dogs-vs-cats-redux-kernels-edition/猫狗分类/TestImages'

in_channels = 3  # 数据集的图片通道数, 彩色为3, 灰度为1
num_classes = 2  # 分类类别（含背景）

spatial_size = (224, 224)
train_transform = [dict(type='LoadImaged', keys='images', ensure_channel_first=True, image_only=False),
                   dict(type='ScaleIntensityd', keys='images'),
                   dict(type='Resized', keys='images', spatial_size=spatial_size, mode='bilinear')]
val_transform = [dict(type='LoadImaged', keys='images', ensure_channel_first=True, image_only=False),
                 dict(type='ScaleIntensityd', keys='images'),
                 dict(type='Resized', keys='images', spatial_size=spatial_size, mode='bilinear')]
batch_size = 16

train_dataloader = dict(batch_size=batch_size, num_workers=0,
                        dataset=dict(type=dataset_type, data_root=data_root, data_suffix='.jpg', subset='train',
                                     test_size=0.2, seed=1234,
                                     transforms=train_transform))
val_dataloader = dict(batch_size=batch_size, num_workers=0,
                      dataset=dict(type=dataset_type, data_root=data_root, data_suffix='.jpg', subset='val',
                                   test_size=0.2, seed=1234,
                                   transforms=val_transform))

test_dataloader = val_dataloader
inferer = dict(type='SimpleInferer')
train_cfg = dict()  # 训练时的配置
val_cfg = dict(inferer=inferer)  # 验证时的配置
test_cfg = dict(inferer=inferer) # 测试时的配置
