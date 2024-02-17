import os
import argparse
import shutil
from medlab.script import train, test, predict

def parse_args():
    # parse arguments
    parser = argparse.ArgumentParser(description='medlab')
    parser.add_argument('--init-path', type=str, default='./', help='config file path')
    return parser.parse_args()

def init_config():
    args  = parse_args()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    source_cfg_dir = os.path.join(current_dir, 'configs')
    target_cfg_dir = os.path.join(args.init_path, 'configs')
    shutil.copytree(source_cfg_dir, target_cfg_dir)

def init_enviroment():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    requirements = os.path.join(os.path.dirname(current_dir), 'requirements.txt')
    os.system('pip install -r {}'.format(requirements))