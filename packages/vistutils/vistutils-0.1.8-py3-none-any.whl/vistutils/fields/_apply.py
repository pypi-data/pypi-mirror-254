"""The apply function decorates method. The actual return value is
another callable which receives the decorated object, sets an attribute on
it and returns it again. Please note that the decorated object does not
get wrapped, but is returned with the attributes set. Use two positional
arguments or any number of keyword arguments."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Callable

from vistutils import monoSpace
from vistutils.fields import AbstractField
from vistutils.waitaminute import EffortException


def apply(*args, **kwargs) -> Callable:
  """The apply function decorates method. The actual return value is
another callable which receives the decorated object, sets an attribute on
it and returns it again. Please note that the decorated object does not
get wrapped, but is returned with the attributes set. Use two positional
arguments or any number of keyword arguments."""
  if args and kwargs:
    e = """Implementing handling of positional arguments mixed with 
    keyword arguments take more effort than the utility is worth. """
    raise EffortException(e)
  if not (args or kwargs):
    e = """Received no arguments specifying decoration!"""
    raise ValueError(e)
  if args:
    if len(args) % 2:
      e = """Expected an even number of positional arguments, but received: 
      %d!"""
      raise ValueError(monoSpace(e % len(args)))
    keys, vals = [], []
    for (i, arg) in enumerate(args):
      if i % 2:  # Is a value
        vals.append(arg)
      else:  # Is a key and must be of type str or field
        if isinstance(arg, (str, AbstractField)):
          keys.append(arg)
        else:
          raise TypeError
    kwargs = {key: val for (key, val) in zip(keys, vals)}
    return apply(**kwargs)

  def decorate(callMeMaybe: Callable) -> Callable:
    """Decorates received callables. """
    for (key, val) in kwargs.items():
      setattr(callMeMaybe, key, val)
    setattr(callMeMaybe, '__is_decorated__', True)
    return callMeMaybe

  return decorate
