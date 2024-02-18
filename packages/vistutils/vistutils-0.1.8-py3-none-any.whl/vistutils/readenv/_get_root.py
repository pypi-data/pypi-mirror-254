"""The getRoot function attempts to locate the root of the current
project."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
import os


def getRoot(dir_: str = None) -> str:
  """The getRoot function attempts to locate the root of the current
project."""
  return os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
