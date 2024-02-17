from timm import create_model, list_models

from medlab.registry import MODELS

# for i in [i for i in list_models() if "tf_" not in i]:
#     MODELS.register_module(name='cls_'+ i, module=create_model)
