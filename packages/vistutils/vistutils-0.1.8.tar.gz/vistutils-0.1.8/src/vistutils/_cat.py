"""The Cats class provides a base class for Enum like classes. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Callable, Union

from vistutils.fields import AbstractField
from vistutils.metas import AbstractMetaclass, BaseNamespace
from vistutils.metas import Bases as BS

from vistutils.metas import Namespace as NS


class CatField(AbstractField):
  """Descriptor for cat class"""

  def __init__(self, *args, **kwargs) -> None:
    AbstractField.__init__(self, *args, **kwargs)

  def __prepare_owner__(self, owner: type) -> type:
    return owner

  def __get__(self, instance: Any, owner: type) -> Any:
    if instance is not None:
      return instance
    return getattr(owner, self.__field_name__)


class CatSpace(BaseNamespace):
  """Namespace class used for CatMeta"""

  def __init__(self, *args, **kwargs) -> None:
    BaseNamespace.__init__(self, *args, **kwargs)
    self.__defined_keys__ = []
    self.__var_space__ = None
    self.__call_space__ = None
    self.__cat_space__ = None

  def __explicit_get_item__(self, key: str, ) -> Any:
    """Reimplementation catching the keys"""
    if key not in self.__defined_keys__:
      self.__defined_keys__.append(key)
    return BaseNamespace.__explicit_get_item__(self, key, )

  def __explicit_set_item__(self, key: str, val: Any, old: Any) -> None:
    """Reimplementation catching the keys"""
    if key not in self.__defined_keys__:
      self.__defined_keys__.append(key)
    return BaseNamespace.__explicit_set_item__(self, key, val, old)

  def __explicit_del_item__(self, key: str, oldVal: Any) -> None:
    """Reimplementation removing keys"""
    if key in self.__defined_keys__:
      self.__defined_keys__ = [k for k in self.__defined_keys__ if
                               k != key]
    return BaseNamespace.__explicit_del_item__(self, key, oldVal)

  def getKeys(self) -> list[str]:
    """Getter-function for the keys"""
    defKeys = self.__defined_keys__
    for (key, val) in self.getAnnotations().items():
      if key not in defKeys:
        defKeys.append(key)
    return defKeys

  def getAnnotations(self) -> dict[str, str]:
    """Getter-functions for annotations"""
    __annotations__ = {}
    for entry in self.__access_log__:
      if entry.get('key', ) == '__annotations__':
        if entry.get('access', ) == 'SET':
          data = entry.get('val', )
          if isinstance(data, dict):
            __annotations__ = {**__annotations__, **data}
    return __annotations__

  def compile(self) -> None:
    """Compiles the final namespace"""
    varSpace = {}
    callSpace = {}
    catSpace = {}
    for key in self.getKeys():
      val = dict.get(self, key, None)
      if callable(val):
        callSpace = {**callSpace, **{key: val}}
      elif key.startswith('__') and key.endswith('__'):
        varSpace = {**varSpace, **{key: val}}

      elif val is None:
        catSpace = {**catSpace, **{key: CatField()}}
    self.__var_space__ = varSpace
    self.__call_space__ = callSpace
    self.__cat_space__ = catSpace


class CatMeta(AbstractMetaclass):
  """The Cats class provides a base class for Enum like classes. """

  @classmethod
  def __prepare__(mcls, name: str, bases: BS, **kwargs) -> NS:
    """Creates and returns the namespace object. """
    namespace = CatSpace(name, bases, **kwargs)
    setattr(namespace, '__meta_class__', mcls)
    return namespace

  @staticmethod
  def strFactory() -> Callable:
    """String conversion factory"""

    def __str__(self, ) -> str:
      """Returns the cat name"""
      if hasattr(self, '__cat_name__'):
        return getattr(self, '__cat_name__')
      raise AttributeError

    return __str__

  @staticmethod
  def intFactory() -> Callable:
    """Integer conversion factory"""

    def __int__(self, ) -> int:
      """Returns the cat value"""
      if hasattr(self, '__cat_value__'):
        return getattr(self, '__cat_value__')
      raise AttributeError

    return __int__

  def __new__(mcls,
              name: str,
              bases: BS,
              namespace: CatSpace,
              **kwargs) -> type:
    namespace.freeze()
    namespace.compile()
    variableSpace = namespace.__var_space__
    callSpace = namespace.__call_space__
    space = {**variableSpace, **callSpace}
    cls = AbstractMetaclass.__new__(mcls, name, (), space, **kwargs)
    catSpace = namespace.__cat_space__
    instances = []
    for (cat, val) in catSpace.items():
      self = type.__call__(cls, )
      setattr(self, '__cat_name__', cat.upper())
      setattr(self, '__cat_value__', len(instances))
      instances.append(self)

    setattr(cls, '__cat_instances__', instances)
    setattr(cls, '__temp_instances__', None)
    setattr(cls, '__int__', mcls.intFactory())
    setattr(cls, '__str__', mcls.strFactory())
    return cls

  def __call__(cls, *args, **kwargs) -> Any:
    """Retrieves the instance matching the arguments"""
    if not args:
      raise ValueError
    if isinstance(args[0], int):
      for cat in cls:
        if int(cat) == args[0]:
          return cat
    if isinstance(args[0], str):
      for cat in cls:
        if getattr(cat, '__cat_name__') == args[0]:
          return cat
    raise AttributeError

  def __iter__(cls) -> Any:
    """Implementation of iteration"""
    setattr(cls, '__temp_instances__', getattr(cls, '__cat_instances__'))
    return cls

  def __next__(cls) -> Any:
    """Implementation of iteration"""
    tempInstances = getattr(cls, '__temp_instances__')
    if tempInstances:
      out = tempInstances.pop(0)
      setattr(cls, '__temp_instances__', tempInstances)
      return out
    raise StopIteration

  def __getitem__(cls, cat: Union[str, int]) -> Any:
    """Looks for cat """
    return cls(cat)

  def __matmul__(cls, other: Any) -> Any:
    """Looks for __class_matmul__ on the class body"""
    if hasattr(cls, '__class_matmul__'):
      func = getattr(cls, '__class_matmul__')
      if callable(func):
        if hasattr(func, '__self__'):
          return func(other)
        return func(cls, other)
      raise TypeError
    raise NotImplemented

  def __rmatmul__(cls, other: Any) -> Any:
    """Calls the regular """
    return cls @ other

  def __getattr__(cls, key: str) -> Any:
    print(cls, key)
    try:
      for self in cls:
        if getattr(self, '__cat_name__').lower() == key.lower():
          return self
    except AttributeError as attributeError:
      raise attributeError


class Cat(metaclass=CatMeta):
  """Enum like class"""

  def __init__(self, *__, **_) -> None:
    pass
