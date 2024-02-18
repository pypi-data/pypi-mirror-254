"""The AbstractDecorator provides a baseclass for decorators. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from vistutils.decorators import DecMeta
from vistutils.fields import Field


class AbstractDecorator(metaclass=DecMeta):
  """The AbstractDecorator provides a baseclass for decorators. """

  __inner_object__ = Field()

  def __init__(self, *args, **kwargs) -> None:
    self.__inner_object__ = None
    self.__inner_return_value__ = None
    self.__inner_args__ = None
    self.__inner_kwargs__ = None

  def _setArgs(self, *args, **kwargs) -> None:
    """Sets the argument for an upcoming call"""
    self.__inner_args__ = args
    self.__inner_kwargs__ = kwargs

  def _setReturnValue(self, returnValue: Any) -> None:
    """Sets the return value received from call to inner object"""
    self.__inner_return_value__ = returnValue

  def _resetCall(self, ) -> None:
    """Resets the arguments and return value before a new call"""
    self.__inner_return_value__ = None
    self.__inner_args__ = None
    self.__inner_kwargs__ = None

  def _invoke(self, **kwargs) -> None:
    """Calls inner object"""
    inner = self._getInnerObject()
    postArgs = self._getArgs()
    keyWordArgs = self._getKwargs()
    self._setReturnValue(inner(*postArgs, **keyWordArgs))

  @__inner_object__.SET
  def _setInnerObject(self, innerObject: Any) -> None:
    """Setter-function for inner object"""
    self.__inner_object__ = innerObject

  @__inner_object__.GET
  def _getInnerObject(self) -> Any:
    """Getter-function for inner object"""
    return self.__inner_object__

  def _getArgs(self) -> list:
    """Getter-function for list of positional arguments"""
    if self.__inner_args__ is None:
      return []
    return [*self.__inner_args__]

  def _getKwargs(self) -> dict:
    """Getter-function for dictionary of keyword arguments"""
    if self.__inner_kwargs__ is None:
      return {}
    return {**self.__inner_kwargs__}

  def _getReturnValue(self) -> Any:
    """Getter-function for return value"""
    return self.__inner_return_value__

  def __call__(self, *args, **kwargs) -> Any:
    """Handles call. If inner object is not set, this method sets it.
Otherwise, a call is made to inner object. """
    if self.__inner_object__ is None:
      if args:
        innerObject = args[0]
        self._setInnerObject(innerObject)
        return self
      raise RuntimeError
    self._resetCall()
    self._setArgs(*args, **kwargs)
    self._invoke(_who=self.__call__.__name__)
    return self._getReturnValue()
