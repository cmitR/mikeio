import clr
import pandas as pd
import numpy as np
import array
import sys
import System
from System import Array
import datetime
import ctypes
from ctypes import string_at
import sys

sys.path.append(r"C:\Program Files (x86)\DHI\2019\bin\x64")
clr.AddReference("DHI.Generic.MikeZero.DFS")
clr.AddReference("DHI.Generic.MikeZero.EUM")
clr.AddReference("System")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("System.Runtime")

import platform
p=platform.architecture()
x64 = False
x64 = '64' in p[0]
if not x64:
    print('This library has not been tested in a 32 bit system!!!!')

from pydhi import dfs0 as dfs0
from pydhi import dfs1 as dfs1
from pydhi import dfs2 as dfs2
from pydhi import dfs3 as dfs3
from pydhi import dfs_util as dfs_util