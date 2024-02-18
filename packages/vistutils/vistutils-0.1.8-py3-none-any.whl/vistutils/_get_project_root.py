"""The getProjectRoot function finds the current project root"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import sys
import os


def getProjectRoot() -> str:
  """The getProjectRoot function finds the current project root"""
  return os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
