from os import remove
from os.path import basename, dirname, exists, join
from shutil import copy
from typing import List

from nwon_deployment.print_output import print_output


def copy_example_files(example_files: List[str], fresh_copy: bool = False):
    for file in example_files:
        if exists(file):
            name = basename(file).replace(".example", "")
            target = join(dirname(file), name)

            if fresh_copy is True:
                remove(target)

            if not exists(target):
                copy(name, target)

            print_output(f"Copied {file} to {target}")


__all__ = ["copy_example_files"]
