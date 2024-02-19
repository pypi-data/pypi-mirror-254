# Copyright (c) 2023 NEC Corporation. All Rights Reserved.

import os.path
import runpy
import sys

from . import importhook
from . import pandas as apandas

# ignore this script itself
importhook.ImportHook.ignore_names.append(os.path.abspath(__file__))

if __name__ == "__main__":
    sys.argv.insert(1, apandas.__name__)
    runpy.run_module(importhook.__name__, run_name=__name__, alter_sys=True)
