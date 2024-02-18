"""The ReadEnvException provides a custom exception class for the readenv
module. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


class ReadEnvException(Exception):
  """ReadEnvException provides a custom exception class for the readenv
module. """

  def __init__(self, *args) -> None:
    msg, baseExc = None, None
    for arg in args:
      if isinstance(arg, str) and msg is None:
        msg = arg
      if isinstance(arg, Exception) and baseExc is None:
        baseExc = arg
    if msg is None:
      e = """readenv module failed because: %s"""
      msg = e % baseExc
    Exception.__init__(self, msg)
