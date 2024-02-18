import os
from pathlib import Path

from cxpm.config import config
from cxpm.tools import download, extract
from cxpm.cmake import CMake

usage = """
find_package(spdlog CONFIG REQUIRED)

target_link_libraries(<target> PRIVATE spdlog) 
or 
target_link_libraries(<target> PRIVATE spdlog::spdlog_header_only)
"""

url_template = (
    "https://github.com/gabime/spdlog/archive/refs/tags/v{version}.zip"
)

class Builder:
    def __init__(self, version="1.13.0"):
        self.name = "spdlog"
        self.version = version
        self.url = url_template.format(version=self.version)
        self.install_dir = f"{config.install_dir}/{self.name}"
        self.usage = usage

    def source(self):
        file_path = download(self.url)
        self.source_dir = extract(file_path)

    def build(self):
        self.cmake = CMake()
        self.cmake.configure(self.source_dir)
        self.cmake.build()

    def install(self):
        self.cmake.install(self.install_dir)

