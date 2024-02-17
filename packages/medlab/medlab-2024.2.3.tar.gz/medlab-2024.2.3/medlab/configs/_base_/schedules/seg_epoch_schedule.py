seed = 1234

task_type = 'BaseSegTask'

# 评估指标, 可为dict或list, MONAI提供的评估指标, 接口详情见MONAI官网
metrics = [dict(type='DiceMetric', include_background=False, reduction='mean'),
           dict(type='ConfusionMatrixMetric', include_background=False, reduction='mean', metric_name='accuracy'),
           dict(type='HausdorffDistanceMetric', include_background=False, percentile=95, reduction='mean'),
           dict(type='MeanIoU', include_background=False, reduction='mean')]

optims = dict(optimizer=dict(type='Adam', lr=0.001),  # lr_scheduler=dict(
              #     scheduler=dict(type='ReduceLROnPlateau', mode='min', factor=0.5, patience=10, min_lr=1e-4),
              #     monitor='DiceMetric',
              #     interval='epoch',
              #     frequency=1
              # )
              )

trainer = dict(type='Trainer',
               logger=[dict(type='TensorBoardLogger', version='tensorboard'), dict(type='CSVLogger', version='csv')],
               devices=[0],
               accelerator='gpu', strategy='auto', precision='32', max_epochs=100, check_val_every_n_epoch=1,
               callbacks=[dict(type='ModelCheckpoint', filename='{epoch}', every_n_epochs=1),
                          dict(type='ModelCheckpoint', monitor='DiceMetric', mode='max', save_top_k=1,
                               filename='{epoch}_{DiceMetric:.4f}'),
                          dict(type='LearningRateMonitor', logging_interval='step')],
               profiler='simple', num_sanity_val_steps=0)

ckpt_path = None
