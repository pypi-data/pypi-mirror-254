import os

from monai.data import Dataset
from sklearn.model_selection import train_test_split

from medlab.registry import DATASETS, TRANSFORMS
import configparser
import pandas as pd


@DATASETS.register_module()
class MedAILabClsDataset(Dataset):
    META_INFO = {'classes': {}}

    def __init__(
            self,
            data_root: str,
            subset: str = None,
            val_size: float = 0.2,
            test_size: float = 0,
            seed: int = 1234,
            transforms: dict = None,
            metainfo: str = '.dataset.medailab',
            annotation_file: str = "classification.csv"
    ):
        assert subset in ['train', 'val', 'test', None], "subset类型错误"
        assert val_size >= 0 and val_size < 1
        assert test_size >= 0 and test_size < 1   
        meta_file = os.path.join(data_root, metainfo)
        annotation_file = os.path.join(data_root, annotation_file)
        assert os.path.exists(meta_file), "meta文件不存在"
        assert os.path.exists(annotation_file), "标注文件不存在"

        config = configparser.ConfigParser()
        config.read(meta_file, encoding='utf8')
        assert "classes" in config.sections(), "meta文件错误"
        options = config.options('classes')
        classes = {}
        for opt in options:
            classes[config.get('classes', opt)] = opt
        self.META_INFO['classes'] = classes

        data = pd.read_csv(annotation_file, header=None)
        data.columns = ["images", "labels"]
        data.drop(data[data['labels'] == -1].index, inplace=True)
        images = data["images"]
        labels = data["labels"]

        images = [os.path.join(data_root, "Images", i) for i in images]
    
        assert len(images) > 0, 'No images found in {}'.format(data_root)
        assert len(images) == len(labels), 'The number of images:{} and labels:{} should be equal'.format(len(images),
                                                                                             len(labels))

        if subset is not None and val_size > 0:
            train_x, tmp_x, train_y, tmp_y = train_test_split(images, labels, test_size=val_size+test_size, random_state=seed,
                                                              stratify=labels)
            if subset == 'train':
                images = train_x
                labels = train_y
            else:
                if test_size == 0:
                    images = tmp_x
                    labels = tmp_y
                else:
                    val_x, test_x, val_y, test_y = train_test_split(tmp_x, tmp_y, test_size=test_size/(val_size+test_size), random_state=seed,
                                                              stratify=tmp_y)
                    if subset == 'val':
                        images = val_x
                        labels = val_y
                    else:
                        images = test_x
                        labels = test_y
        data = [{'images': i, 'labels': m} for i, m in zip(images, labels)]
        if transforms is None:
            transforms = []
        transforms = TRANSFORMS.build(transforms)
        super().__init__(data=data, transform=transforms)

    @property
    def classes(self):
        return self.META_INFO['classes']


@DATASETS.register_module()
class MedAILabSegDataset(Dataset):
    META_INFO = {'classes': {}}

    def __init__(
            self,
            data_root: str,
            subset: str = None,
            val_size: float = 0.2,
            test_size: float = 0,
            seed: int = 1234,
            transforms: dict = None,
            metainfo: str = '.dataset.medailab',
            annotation_dir: str = "Segmentation"
    ):
        print("data_root", data_root)
        assert subset in ['train', 'val', 'test', None], "subset类型错误"
        assert val_size >= 0 and val_size < 1
        assert test_size >= 0 and test_size < 1   
        meta_file = os.path.join(data_root, metainfo)
        image_dir = os.path.join(data_root, "Images")
        annotation_dir = os.path.join(data_root, annotation_dir)
        assert os.path.exists(meta_file), "meta文件不存在"
        assert os.path.exists(annotation_dir), "标注目录不存在"

        config = configparser.ConfigParser()
        config.read(meta_file, encoding='utf8')
        assert "classes" in config.sections(), "meta文件错误"
        options = config.options('classes')
        classes = {}
        for opt in options:
            classes[config.get('classes', opt)] = opt
        self.META_INFO['classes'] = classes

        images = []
        labels = []
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                images.append(os.path.join(root, file))
                labels.append(os.path.join(root.replace(image_dir, annotation_dir), file))

        assert len(images) > 0, 'No images found in {}'.format(data_root)
        assert len(images) == len(labels), 'The number of images:{} and labels:{} should be equal'.format(len(images),
                                                                                             len(labels))

        print("数据集长度：", len(images), len(labels))

        if subset is not None and val_size > 0:
            train_x, tmp_x, train_y, tmp_y = train_test_split(images, labels, test_size=val_size+test_size, random_state=seed)
            if subset == 'train':
                images = train_x
                labels = train_y
            else:
                if test_size == 0:
                    images = tmp_x
                    labels = tmp_y
                else:
                    val_x, test_x, val_y, test_y = train_test_split(tmp_x, tmp_y, test_size=test_size/(val_size+test_size), random_state=seed)
                    if subset == 'val':
                        images = val_x
                        labels = val_y
                    else:
                        images = test_x
                        labels = test_y
        data = [{'images': i, 'labels': m} for i, m in zip(images, labels)]
        if transforms is None:
            transforms = []
        transforms = TRANSFORMS.build(transforms)
        super().__init__(data=data, transform=transforms)

    @property
    def classes(self):
        return self.META_INFO['classes']