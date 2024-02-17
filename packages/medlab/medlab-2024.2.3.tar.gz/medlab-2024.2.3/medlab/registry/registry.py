from mmengine.registry import Registry

from .build_functions import build_model_from_cfg, build_logger_from_cfg, build_callback_from_cfg, \
    build_transform_from_cfg, build_metric_from_cfg

# manage PyTorch-lightning Trainer
TRAINERS = Registry('trainer', locations=['medlab.core'], scope='medlab')
# manage PyTorch-lightning Callbacks
CALLBACKS = Registry('callback', build_func=build_callback_from_cfg, locations=['medlab.core.callbacks'], scope='medlab')
# manage PyTorch-lightning loggers
LOGGERS = Registry('logger', build_func=build_logger_from_cfg, locations=['medlab.core.loggers'], scope='medlab')
# manage different vision tasks based on LightningModule
TASKS = Registry('task', locations=['medlab.tasks'], scope='medlab')

# manage datasets
DATASETS = Registry('dataset', locations=['medlab.datasets'], scope='medlab')
# manage MONAI transforms
TRANSFORMS = Registry('transform', build_func=build_transform_from_cfg, locations=['medlab.core.transforms'], scope='medlab')
# manage MONAI inferers
INFERERS = Registry('inferer', locations=['medlab.core.inferers'], scope='medlab')

# manage PyTorch models
MODELS = Registry('model', build_func=build_model_from_cfg, locations=['medlab.models'], scope='medlab')
LOSSES = Registry('loss', locations=['medlab.core.losses'], scope='medlab')
OPTIMIZERS = Registry('optimizer', locations=['medlab.core.optimizers'], scope='medlab')
LR_SCHEDULERS = Registry('learning rate scheduler', locations=['medlab.core.lr_schedulers'], scope='medlab')
METRICS = Registry('metric', build_func=build_metric_from_cfg, locations=['medlab.core.metrics'], scope='medlab')
