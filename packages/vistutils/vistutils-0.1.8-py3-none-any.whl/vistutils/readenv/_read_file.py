"""The readFile function receives a file path and returns a list of
strings each representing a line in the file."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from vistutils import monoSpace
from vistutils.readenv import ReadEnvException


def readFile(fid: str, **kwargs) -> list[str]:
  """The readFile function receives a file path and returns a list of
strings each representing a line in the file."""

  if not os.path.exists(fid):
    if kwargs.get('strict', True):
      e = """The file '%s' does not exist."""
      exc = FileNotFoundError(monoSpace(e % fid))
      raise ReadEnvException(exc, e)
    else:
      return []

  if os.path.isdir(fid):
    if kwargs.get('strict', True):
      e = """Expected a file, but received a directory: '%s'."""
      exc = IsADirectoryError(monoSpace(e % fid))
      raise ReadEnvException(exc, e)
    else:
      return []

  try:
    with open(fid, 'r') as f:
      return f.readlines()
  except PermissionError as permissionError:
    raise ReadEnvException(permissionError)
