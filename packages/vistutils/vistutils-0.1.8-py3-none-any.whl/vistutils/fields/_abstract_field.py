"""The AbstractField defines an abstract baseclass for descriptor classes.
The baseclass defines how the field name and owner should be defined
automatically by the __set_name__ method. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod


class AbstractField:
  """The AbstractField defines an abstract baseclass for descriptor
classes."""

  def __init__(self, *args, **kwargs) -> None:
    self.__field_name__ = None
    self.__field_owner__ = None

  def __set_name__(self, owner: type, name: str) -> None:
    self.__field_owner__ = owner
    self.__field_name__ = name
    self.__prepare_owner__(owner)

  @abstractmethod
  def __prepare_owner__(self, owner: type) -> type:
    """This special abstract method must be implemented by subclasses to
install this field into it."""

  def _getFieldOwner(self) -> type:
    """Getter-function for field owner"""
    if self.__field_owner__ is not None:
      if isinstance(self.__field_owner__, type):
        return self.__field_owner__
      e = typeMsg('__field_owner__', self.__field_owner__, type)
      raise TypeError(e)
    raise RuntimeError

  def _getFieldName(self) -> str:
    """Getter-function for field name"""
    if self.__field_name__ is not None:
      if isinstance(self.__field_name__, str):
        return self.__field_name__
      e = typeMsg('__field_name__', self.__field_name__, str)
      raise TypeError(e)
    raise RuntimeError

  def _getPrivateName(self) -> str:
    """Getter-function for private name"""
    return '_%s' % self.__field_name__

  def _getCapName(self) -> str:
    """Getter-function for the capitalized version of the name"""
    out, first, fieldName = '', True, self._getFieldName()
    first = True
    for char in fieldName:
      if char == '_':
        out = '%s_' % out
      elif first:
        out = '%s%s' % (out, char.upper())
        first = False
      else:
        out = '%s%s' % (out, char)
    return out
