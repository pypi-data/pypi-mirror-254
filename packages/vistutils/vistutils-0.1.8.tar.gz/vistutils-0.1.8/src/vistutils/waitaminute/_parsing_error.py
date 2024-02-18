"""ParsingError should be raised when no available parsing function
yielded a desired result from given arguments."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils import maybeType
from vistutils.waitaminute import EffortException


class ParsingError(Exception):
  """ParsingError should be raised when no available parsing function
yielded a desired result from given arguments."""

  def __init__(self, *args, **kwargs) -> None:
    if args and kwargs:
      e = """Found both positional and keyword arguments. Implementing 
      support for such mixing takes more effort than the utility it might 
      provide."""
      Exception.__init__(self, maybeType(str, *args))
      raise EffortException(e) from self
    if args:
      if len(args) == 1:
        arg = args[0]
        if isinstance(arg, bytes):
          arg = arg.decode('utf-8')
        if isinstance(arg, str):
          Exception.__init__(self, arg)
      if len(args) > 1:
        strArg = maybeType(str, *args)
        Exception.__init__(self, maybeType(str, *args))
