import os
import configparser

class Config:
    def __init__(self):
        conf = configparser.ConfigParser()
        default_config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        user_config_path = os.path.expanduser("~/.cxpm/config.ini")
        conf.read([default_config_path, user_config_path])

        self.catch_dir = conf['global']['cache_dir']
        self.install_dir = conf['global']['install_dir']
        self.download_dir = f"{self.catch_dir}/download"
        self.build_dir = f"{self.catch_dir}/build"
        self.toolchain = "vs2019"

config = None

def init():
    global config
    config = Config()