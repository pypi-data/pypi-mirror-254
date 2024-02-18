import sys
from typing import List, Optional
import argparse
import importlib

import cxpm.config


def main(args: (Optional[List[str]]) = None) -> int:
    cxpm.config.init()

    parser = argparse.ArgumentParser(
        description="Install packages.", usage="cxpm install <package>"
    )
    parser.add_argument("command", help="The command to execute.")
    parser.add_argument("package", help="The package to install.")
    args = parser.parse_args(args)

    if args.command != "install":
        parser.print_help()
        return 1

    module = importlib.import_module(f"cxpm_builders.{args.package}.builder")
    Builder = getattr(module, "Builder")

    builder = Builder()
    builder.source()
    builder.build()
    builder.install()

    print(f"Installed {builder.name} {builder.version}")
    print(f"Usage: {builder.usage}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
