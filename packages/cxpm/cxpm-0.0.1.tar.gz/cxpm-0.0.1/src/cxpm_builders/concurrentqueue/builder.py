from cxpm.config import config
from cxpm.tools import download, extract
from cxpm.cmake import CMake

usage = """
find_package(concurrentqueue CONFIG REQUIRED)
target_link_libraries(<target> concurrentqueue::concurrentqueue)
"""

url_template = (
    "https://github.com/cameron314/concurrentqueue/archive/refs/tags/v{version}.zip"
)


class Builder:
    def __init__(self, version="1.0.4"):
        self.name = "concurrentqueue"
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

    def install(self):
        self.cmake.install(self.install_dir)
