import os
from pathlib import Path

from .config import config
from .shell import cmd

# vcvarsall_path = r"C:\Program Files\Microsoft Visual Studio\2022\Professional\VC\Auxiliary\Build\vcvarsall.bat"
# set_vs_env = f'call "{vcvarsall_path}" x64'
# toolset_setenv = {
#     "auto": 'echo "auto"',
#     "vs2019": f'call "C:\\Program Files\\Microsoft Visual Studio\\2022\\Professional\\VC\\Auxiliary\\Build\\vcvarsall.bat" x64',
# }

TOOLCHAIN = config.toolchain
BUILD_TYPES = ["Debug", "Release"]
TOOLCHAIN_COMMANDS = {
    "vs2019": f'call "C:\\Program Files\\Microsoft Visual Studio\\2022\\Professional\\VC\\Auxiliary\\Build\\vcvarsall.bat" x64'
}


class CMake:
    def configure(self, source_dir, cache_variables={}):
        self.setenv = TOOLCHAIN_COMMANDS[TOOLCHAIN]
        self.source_dir = Path(source_dir)
        self.build_dir = Path(self.source_dir) / "build"
        os.makedirs(self.build_dir, exist_ok=True)

        cache_flags = ""
        for key, value in cache_variables.items():
            cache_flags += f"-D{key}={value} "

        for type in BUILD_TYPES:
            cache_flags += f"-DCMAKE_BUILD_TYPE:STRING={type}"
            cmd(
                f"{self.setenv} && cmake -S{self.source_dir} -B{self.build_dir}/{type} -G Ninja {cache_flags}"
            )

    def build(self):
        for type in BUILD_TYPES:
            cmd(f"{self.setenv} && cmake --build {self.build_dir}/{type}")

    def install(self, install_dir):
        for type in BUILD_TYPES:
            cmd(f"cmake --install {self.build_dir}/{type} --prefix {install_dir}")

    # def configure_msvc(self):
    #     vcvarsall_path = r"C:\Program Files\Microsoft Visual Studio\2022\Professional\VC\Auxiliary\Build\vcvarsall.bat"
    #     command = f'call "{vcvarsall_path}" x64 && cmake -S{self.source_path} -B{self.build_path} -G Ninja'
    #     cmd(command)
