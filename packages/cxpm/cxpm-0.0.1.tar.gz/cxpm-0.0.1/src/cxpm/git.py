import os
from .tools import cmd

from .config import config

BUILD_DIR = config.build_dir


def clone(url, path=BUILD_DIR):
    project_name = os.path.splitext(os.path.basename(url))[0]
    project_path = os.path.join(path, project_name)
    cmd(f"git clone --depth 1 {url} {project_path}")
    return project_path
