import os
from cxpm.config import config
from cxpm.tools import download, extract
from cxpm.cmake import CMake

usage = """
find_package(autosdk CONFIG REQUIRED)
target_link_libraries(<target> autosdk)
"""

url_template = (
    "ftp://navinfo:123.com123.Com@10.51.29.242/DevOps/Official_Version/HongQi/{version}/SDK/Windows"
)


class Builder:
    def __init__(self, version="20240125"):
        self.name = "autosdk"
        self.version = version
        self.url = url_template.format(version=self.version)
        self.install_dir = f"{config.install_dir}/{self.name}"
        self.usage = usage

    def source(self):
        file_path = download(self.url)
        self.source_path = extract(file_path)

    def build(self):
        self.cmake = CMake()
        self.cmake.configure(self.source_path)
        self.cmake.build()

    def install(self):
        self.cmake.install(self.install_dir)
