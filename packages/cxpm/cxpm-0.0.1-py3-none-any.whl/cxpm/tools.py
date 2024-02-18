import subprocess
import sys
import os
import zipfile
from pathlib import Path
import urllib.request
import http.client
import shutil
import cgi
import glob
import locale
import select

from .config import config

DOWNLOAD_DIR = config.download_dir
BUILD_DIR = config.build_dir
INSTALL_DIR = config.install_dir


def download(url, filename=None, download_dir=DOWNLOAD_DIR):
    response = urllib.request.urlopen(url)

    # 如果没有提供文件名，尝试从Content-Disposition头部获取
    if filename is None:
        cd = response.headers.get("content-disposition")
        if cd:
            value, params = cgi.parse_header(cd)
            filename = params.get("filename")

        # 如果Content-Disposition头部不存在或者没有文件名，使用URL的路径部分
        if filename is None:
            filename = os.path.basename(urllib.parse.urlsplit(url).path)

    file_path = os.path.join(download_dir, filename)
    temp_file_path = f"{file_path}.download"

    # 如果文件已经存在，不再下载
    if os.path.exists(file_path):
        print(f"File {file_path} already exists. Skipping download.")
        return file_path

    os.makedirs(download_dir, exist_ok=True)
    try:
        with open(temp_file_path, "wb") as file:
            file.write(response.read())
    except http.client.IncompleteRead as e:
        print(
            f"Warning: Only {len(e.partial)} out of {e.expected} bytes received. The file might be incomplete."
        )

    # 重命名临时文件（移除.download后缀）
    os.rename(temp_file_path, file_path)

    return file_path


def get_zip_root(file_path):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        names = zip_ref.namelist()

    root_dirs = {name.split("/")[0] for name in names}

    if len(root_dirs) == 1:
        return list(root_dirs)[0]
    else:
        return None


def extract(file_path, extract_path=BUILD_DIR):
    zip_root = get_zip_root(file_path)
    if zip_root is not None:
        # 如果有顶层文件夹，解压到extract_path
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)
        # 返回解压后的文件夹路径
        return str(Path(extract_path) / zip_root)
    else:
        # 如果没有顶层文件夹，根据zip包的名称（去掉后缀）创建新文件夹
        zip_name = Path(file_path).stem
        new_dir = Path(extract_path) / zip_name
        new_dir.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(new_dir)
        # 返回新创建的文件夹路径
        return str(new_dir)


def copy(src_path, dest_path):
    if os.path.isfile(src_path):
        shutil.copy(src_path, dest_path)
    elif os.path.isdir(src_path):
        dest_dir = os.path.join(dest_path, os.path.basename(src_path))
        shutil.copytree(src_path, dest_dir)
    else:
        for path in glob.glob(str(src_path)):
            copy(path, dest_path)
