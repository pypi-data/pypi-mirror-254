# SPDX-License-Identifier: MIT
# Copyright 2021 (c) BayLibre, SAS
# Author: Fabien Parent <fparent@baylibre.com>

import pkg_resources
import platform
import subprocess
import sys

def main():
    mach = platform.machine().lower()
    system = platform.system().lower()
    bin_name = f'bin/{mach}/{system}/bootrom-tool'
    if platform.system() == "Windows":
        bin_name += ".exe"

    binary = pkg_resources.resource_filename('aiot_bootrom', bin_name)
    sys.argv[0] = binary

    try:
        subprocess.run(sys.argv, check=True)
    except KeyboardInterrupt:
        pass
