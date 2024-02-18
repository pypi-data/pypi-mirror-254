"""AbstractNameSpace provides an abstract baseclass allowing for custom
classes to create namespace objects that are suitable for use in custom
metaclasses. Subclasses of this class that adhere refrain from
reimplementing the item accessor methods directly, can generally be
expected to not directly cause errors. Instead of reimplementing
__getitem__, __setitem__ or __delitem__ directly, the baseclass provides
the following methods: __explicit_get_item__, __explicit_set_item__ and
__explicit_del_item__ which are invoked by the __getitem__, __setitem__
and __delitem__ respectively. These default those defined on built in
'dict' class, but subclasses are free to change them."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod
from typing import Any


class AbstractNamespace(dict):
  """AbstractNameSpace an abstract baseclass for custom namespace classes
used in custom metaclasses."""

  def __init__(self, *args, **kwargs) -> None:
    dict.__init__(self, *args, **kwargs)
    self.__access_log__ = []
    self.__update_log__ = True

  def _logGet(self, key: str, val: Any, ) -> None:
    """Logs the results of item retrieval"""
    if self.__update_log__:
      entry = {'access': 'GET', 'key': key, 'val': val}
      self.__access_log__.append(entry)

  def _logSet(self, key: str, oldVal: Any, newVal: Any) -> None:
    """Logs the results of item setting"""
    if self.__update_log__:
      entry = {'access': 'SET', 'key': key,
               'oldVal': oldVal, 'newVal': newVal, 'val': newVal}
      self.__access_log__.append(entry)

  def _logDel(self, key: str, oldVal: Any) -> None:
    """Logs the results of item deletion."""
    if self.__update_log__:
      entry = {'access': 'DEL', 'key': key, 'oldVal': oldVal}
      self.__access_log__.append(entry)

  def freeze(self) -> None:
    """When this instance arrives in the __new__ method in the metaclass,
invoke this method to disable logging."""
    self.__update_log__ = False

  @abstractmethod
  def __explicit_get_item__(self, key: str, ) -> Any:
    """Explicit item retrieval. Subclasses are free to implement this
    method. By default, the parent method from 'dict' is called.
    :param key: The key to retrieve
    :type key: str
    :return: The value return by the namespace in response to the key
    :rtype: Any
    """

  @abstractmethod
  def __explicit_set_item__(self, key: str, Val: Any, old: Any) -> None:
    """Explicit item value setting.  Subclasses are free to implement this
    method. By default, the parent method from 'dict' is called.
    :param key: The key to set
    :type key: str
    :param Val: The new value attempted to be set at given key
    :type Val: Any
    :param old: The existing value returned on the given key
    :type old: Any
    """

  @abstractmethod
  def __explicit_del_item__(self, key: str, oldVal: Any) -> None:
    """Explicit item deletion. Subclasses are free to implement this
    method. By default, the parent method from 'dict' is called.
    :param key: The key to delete
    :type key: str
    :param oldVal: The existing value returned on the given key
    :type oldVal: Any
    """

  def __getitem__(self, key: str) -> Any:
    """Item retrieval. Subclasses must not reimplement this method!
    :param key: The key to retrieve
    :type key: str
    :return: The value return by the namespace in response to the key
    :rtype: Any
    """
    try:
      dict.__getitem__(self, key)
    except KeyError as keyError:
      self._logGet(key, keyError)
      raise keyError
    val = self.__explicit_get_item__(key, )
    self._logGet(key, val, )
    return val

  def __setitem__(self, key: str, val: Any) -> None:
    """Item setting. Subclass must not reimplement this method!
:param key: The key to set
:type key: str
:param val: The new value attempted to be set at given key
:type val: Any"""
    oldVal = None
    if key in self:
      oldVal = dict.__getitem__(self, key)
    self._logSet(key, oldVal, val, )
    self.__explicit_set_item__(key, val, oldVal)

  def __delitem__(self, key: str) -> None:
    """Item deletion. Subclass must not reimplement this method!
:param key: The key to delete
:type key: str"""
    if key in self:
      oldVal = dict.__getitem__(self, key)
      self._logDel(key, oldVal)
      return self.__explicit_del_item__(key, oldVal)
    self._logDel(key, None)
    raise KeyError(key)
