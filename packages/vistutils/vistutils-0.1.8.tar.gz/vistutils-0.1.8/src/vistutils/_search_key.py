"""The searchKey function looks for values in keyword arguments by key."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any


def searchKey(*args, **kwargs) -> Any:
  """The searchKey function looks for values in keyword arguments by key."""
  keys = []
  types = []
  for arg in args:
    if isinstance(arg, str):
      keys.append(arg)
    if isinstance(arg, type):
      types.append(arg)
  for key in keys:
    val = kwargs.get(key, None)
    if val is not None:
      if types:
        if isinstance(val, (*types,)):
          return val
      else:
        return val
  if kwargs.get('_recursion', False):
    return None
  keys = [key.lower() for key in keys]
  return searchKey(*types, *keys, _recursion=True, **kwargs)
