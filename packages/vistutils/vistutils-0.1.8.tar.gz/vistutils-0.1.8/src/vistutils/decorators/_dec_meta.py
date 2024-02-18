"""DecMeta provides a metaclass for the creation of flexible decorators."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from vistutils import monoSpace
from vistutils.decorators import DecSpace
from vistutils.metas import AbstractMetaclass, Bases


class DecMeta(AbstractMetaclass):
  """DecMeta provides a metaclass for the creation of flexible decorators."""

  @classmethod
  def __prepare__(mcls, name: str, bases: Bases, **kwargs) -> DecSpace:
    """Creates the namespace object"""
    return DecSpace(mcls, name, bases, **kwargs)

  def __new__(mcls,
              name: str,
              bases: Bases,
              namespace: DecSpace,
              **kwargs) -> type:
    namespace.freeze()
    cls = AbstractMetaclass.__new__(mcls, name, bases, namespace,
                                    **kwargs)
    return cls

  def __call__(cls, *args, **kwargs) -> Any:
    """This implementation handles the case where the created decorator
class is used without instantiation. Derived classes should implement
a class method named '__class_call__' to define this behaviour. """
    for (key, val) in cls.__dict__.items():
      if callable(val) and hasattr(val, '__isabstractmethod__'):
        if getattr(val, '__isabstractmethod__'):
          raise TypeError(
            'Attempted to instantiate abstract class!')
    classCall = getattr(cls, '__class_call__', None)
    if classCall is None:
      return AbstractMetaclass.__call__(cls, *args, **kwargs)
    if callable(classCall):
      if hasattr(classCall, '__self__'):
        return classCall(*args, **kwargs)
      return classCall(cls, *args, **kwargs)
    e = """Attribute named: '%s' was: '%s' of type: '%s', but only 
    callables are allowed here!"""
    name = '__class_call__'
    item = classCall
    actType = type(classCall)
    raise TypeError(monoSpace(e % (name, item, actType,)))
