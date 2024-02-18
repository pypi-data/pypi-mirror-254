from cxpm.config import config
from cxpm.tools import download, extract
from cxpm.cmake import CMake

usage = """
find_package(Eigen3 CONFIG REQUIRED)
target_link_libraries(<target> Eigen3::Eigen)
"""

url_template = (
    "https://gitlab.com/libeigen/eigen/-/archive/{version}/eigen-{version}.zip"
)


class Builder:
    def __init__(self, version="3.4.0"):
        self.name = "eigen3"
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

    def install(self):
        self.cmake.install(self.install_dir)
