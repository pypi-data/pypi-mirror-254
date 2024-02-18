"""Field is a descriptor class. Use with the Acc enum class with
instances: GET, SET and DEL to decorate getter, setter and deleter
methods. Please note, that the decorator does not wrap the method.
Instead, a reference will point the field to decorated method. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Callable, Any

from vistutils.fields import AbstractField


class Field(AbstractField):
  """Field is a descriptor class. Use with the Acc enum class with
instances: GET, SET and DEL to decorate getter, setter and deleter
methods. Please note, that the decorator does not wrap the method.
Instead, a reference will point the field to decorated method. """

  def __init__(self, *args, **kwargs) -> None:
    AbstractField.__init__(self, *args, **kwargs)
    self.__getter_function__ = None
    self.__setter_function__ = None
    self.__deleter_function__ = None

  def __prepare_owner__(self, owner: type) -> type:
    """Implementation of the abstract method"""
    return owner

  def _setGetter(self, callMeMaybe: Callable) -> Callable:
    """Sets the getter"""
    if hasattr(callMeMaybe, '__func__'):
      self.__getter_function__ = callMeMaybe.__func__
    else:
      self.__getter_function__ = callMeMaybe
    return callMeMaybe

  def _getGetter(self, ) -> Callable:
    """Getter-function for the getter"""
    return self.__getter_function__

  def _setSetter(self, callMeMaybe: Callable) -> Callable:
    """Sets the setter"""
    if hasattr(callMeMaybe, '__func__'):
      self.__setter_function__ = callMeMaybe.__func__
    else:
      self.__setter_function__ = callMeMaybe
    return callMeMaybe

  def _getSetter(self, ) -> Callable:
    """Getter-function for the getter"""
    return self.__setter_function__

  def _setDeleter(self, callMeMaybe: Callable) -> Callable:
    """Sets the deleter"""
    if hasattr(callMeMaybe, '__func__'):
      self.__deleter_function__ = callMeMaybe.__func__
    else:
      self.__deleter_function__ = callMeMaybe
    return callMeMaybe

  def _getDeleter(self, ) -> Callable:
    """Getter-function for the getter"""
    return self.__deleter_function__

  def __get__(self, instance: Any, owner: type) -> Any:
    """Implementation of getter"""
    getter = self._getGetter()
    if getter is None:
      raise AttributeError('Getter function not defined!')
    return getter(owner) if instance is None else getter(instance)

  def __set__(self, instance: Any, value: Any) -> None:
    """Implementation of setter"""
    setter = self._getSetter()
    if setter is None:
      raise AttributeError('Setter function not defined!')
    return setter(instance, value)

  def __delete__(self, instance) -> None:
    """Implementation of deleter"""
    deleter = self._getDeleter()
    if deleter is None:
      raise AttributeError('Deleter function not defined!')
    return delattr(instance, self.__field_name__)

  def GET(self, callMeMaybe: Callable) -> Callable:
    """Alias for setting the getter"""
    return self._setGetter(callMeMaybe)

  def SET(self, callMeMaybe: Callable) -> Callable:
    """Alias for setting the setter"""
    return self._setSetter(callMeMaybe)

  def DEL(self, callMeMaybe: Callable) -> Callable:
    """Alias for setting the deleter"""
    return self._setDeleter(callMeMaybe)
