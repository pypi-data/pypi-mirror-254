import os
from pathlib import Path

from cxpm.config import config
from cxpm.tools import download, extract, copy
from cxpm.cmake import CMake

usage = """
find_package(asio CONFIG REQUIRED)
target_link_libraries(<target> asio)
"""

url_template = (
    "https://codeload.github.com/chriskohlhoff/asio/zip/refs/tags/asio-{version}"
)

class Builder:
    def __init__(self, version="1.29.0"):
        self.name = "asio"
        self.version = version
        self.url = url_template.format(version=self.version.replace('.', '-'))
        self.install_dir = f"{config.install_dir}/{self.name}"
        self.usage = usage

    def source(self):
        file_path = download(self.url)
        self.source_path = extract(file_path)

    def build(self):
        current_script_path = os.path.dirname(os.path.realpath(__file__))
        cmake_scripts = Path(current_script_path) / 'cmake' / '*'
        copy(cmake_scripts, self.source_path)

        self.cmake = CMake()
        self.cmake.configure(self.source_path)

    def install(self):
        self.cmake.install(self.install_dir)
