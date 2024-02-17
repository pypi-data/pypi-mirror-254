from lightning.pytorch.callbacks import ModelCheckpoint, LearningRateMonitor, EarlyStopping

from medlab.registry import CALLBACKS

CALLBACKS.register_module(name='ModelCheckpoint', module=ModelCheckpoint)
CALLBACKS.register_module(name='LearningRateMonitor', module=LearningRateMonitor)
CALLBACKS.register_module(name='EarlyStopping', module=EarlyStopping)
