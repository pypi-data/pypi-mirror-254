"""BaseNamespace subclasses the AbstractNamespace and provides standard
dictionary behaviour, but includes logging of item accessor method calls. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from vistutils.metas import AbstractNamespace, Bases


class BaseNamespace(AbstractNamespace):
  """BaseNamespace subclasses the AbstractNamespace and provides standard
dictionary behaviour, but includes logging of item accessor method
calls. """

  def __init__(self, name: str, bases: Bases, **kwargs) -> None:
    AbstractNamespace.__init__(self, **kwargs)
    self.__class_name__ = name
    self.__class_bases__ = bases
    self.__kwargs__ = kwargs
    self.__meta_class__ = None

  def setMetaclass(self, mcls: type) -> None:
    """Setter-function for the metaclass"""
    self.__meta_class__ = mcls

  def __explicit_get_item__(self, key: str, ) -> Any:
    """Implementation of item retrieval"""
    return dict.__getitem__(self, key)

  def __explicit_set_item__(self, key: str, val: Any, old: Any) -> None:
    """Implementation of item value setting"""
    return dict.__setitem__(self, key, val)

  def __explicit_del_item__(self, key: str, oldVal: Any) -> None:
    """Implementation of entry deletion. """
    return dict.__delitem__(self, key)
