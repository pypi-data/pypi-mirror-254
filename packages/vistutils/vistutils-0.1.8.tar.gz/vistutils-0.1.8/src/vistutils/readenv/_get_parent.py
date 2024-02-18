"""The getParent function receives a path and returns the parent to the
depth indicated by the second parameter. By default, this is 1 which
indicate the immediate parent. If no path is given the path of __file__ is
used instead. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from vistutils import monoSpace


def getParent(*args, **kwargs) -> str:
  """Finds parent path"""
  allowFile = kwargs.get('allowFile', True)
  requireExist = kwargs.get('requireExist', False)
  depth = None
  altNum = None
  directory = None
  for arg in args:
    if isinstance(arg, int) and depth is None:
      depth = arg if arg > 0 else -arg
    if isinstance(arg, str) and directory is None:
      directory = arg
    if isinstance(arg, float) and altNum is None:
      if (round(arg) - arg) ** 2 < 1e-06:
        altNum = int(arg) if arg > 0 else -int(arg)
  altNum = 1 if altNum is None else altNum
  depth = altNum if depth is None else depth
  if directory is None:
    directory = os.path.dirname(os.path.abspath(__file__))
  if os.path.isfile(directory) and allowFile:
    directory = os.path.dirname(directory)
  elif os.path.isfile(directory):
    e = """getParent received file: '%s' with allowFile flag set to False!"""
    raise NotADirectoryError(monoSpace(e % directory))
  if not depth:
    return directory
  directory = os.path.normcase(os.path.join(directory, '..'))
  return getParent(directory, depth - 1)
