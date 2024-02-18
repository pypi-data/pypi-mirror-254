import os

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
    "https://github.com/msgpack/msgpack-c/archive/refs/tags/cpp-{version}.zip"
)


class Builder:
    def __init__(self, version="6.1.0"):
        self.name = "msgpack-cxx"
        self.version = version
        self.url = url_template.format(version=self.version)
        self.install_dir = f"{config.install_dir}/{self.name}"
        self.usage = usage

    def source(self):
        file_path = download(self.url)
        self.source_dir = extract(file_path)

    def build(self):
        self.cmake = CMake()
        self.cmake.configure(
            source_dir=self.source_dir, cache_variables={"MSGPACK_USE_BOOST": "OFF"}
        )

    def install(self):
        self.cmake.install(self.install_dir)
