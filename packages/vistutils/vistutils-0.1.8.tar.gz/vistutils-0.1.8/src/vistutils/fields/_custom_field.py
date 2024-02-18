"""The CustomField provides a highly flexible descriptor class. Use the
'apply' decorator method to decorate methods with a key value pair, with the
key indicating the name of the field this method relates to and the value
describing what access the method provides.

When instantiating the CustomField, the first positional argument can be
used to set a default value. This value is then retrieved by calling
'getDefault' on the field instance itself. Please note that it is the
responsibility of the owning class to implement adequate accessor methods
using the apply decorator as described."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from vistutils import monoSpace, maybe
from vistutils.fields import AbstractField


class CustomField(AbstractField):
  """The CustomField provides a highly flexible descriptor class. Use the
'apply' decorator method to decorate methods with a key value pair,
with the key indicating the name of the field this method relates to and
the value describing what access the method provides."""

  def __init__(self, *args, **kwargs) -> None:
    self.__default_value__ = None
    self.__getter_function__ = None
    self.__setter_function__ = None
    self.__deleter_function__ = None
    self.__req_get__ = kwargs.get('requireGetter', True)
    self.__req_set__ = kwargs.get('requireSetter', False)
    self.__req_del__ = kwargs.get('requireDeleter', False)
    AbstractField.__init__(self, *args, **kwargs)
    if args:
      self.__default_value__ = args[0]

  def getDefaultValue(self) -> Any:
    """Returns the default value if present. If not, raises AttributeError"""
    if self.__default_value__ is None:
      e = """This CustomField instance received no default value at 
      instantiation, but now received call to getter function for the 
      default value!"""
      raise AttributeError(monoSpace(e))
    return self.__default_value__

  def __prepare_owner__(self, owner) -> type:
    """Implementation of abstract method which searches the namespace of
the owning class for the methods that match the field name of the
field instance. Please note that the field name is automatically
inferred by the __set_name__ method inherited from the abstract
baseclass."""
    for (key, val) in owner.__dict__.items():
      if callable(val):
        if hasattr(val, '__is_decorated__'):
          if hasattr(val, self.__field_name__):
            accessor = getattr(val, self.__field_name__)
            if accessor.lower() in ['get', 'set', 'delete']:
              acc = accessor.lower()
              if acc == 'get' and self.__getter_function__ is None:
                self.__getter_function__ = val
              elif acc == 'get':
                e = """Received second getter function!"""
                raise NameError(e)

              if acc == 'set' and self.__setter_function__ is None:
                self.__setter_function__ = val
              elif acc == 'set':
                e = """Received second setter function!"""
                raise NameError(e)

              if acc == 'delete' and self.__deleter_function__ is None:
                self.__deleter_function__ = val
              elif acc == 'delete':
                e = """Received second deleter function!"""
                raise NameError(e)
    if self.__getter_function__ is None and self.__req_get__:
      e = """Owners of CustomField instances must implement at least the 
      getter function. This error is raised immediately following the 
      __set_name__ method, but before the owning class has been passed to 
      class decorators. The expected behaviour is that method decorators 
      such as 'apply' receive the methods before they are passed to the 
      namespace object during class creation. This implies that method 
      decorators must have returned before this method has been invoked. 
      <br><br>
      If this error message keeps appearing, the recommendation is to 
      place breakpoints or similar to track the order of events. If the 
      owner class is being subclassed, the expected behaviour is somewhat 
      unclear. In particular, the effects of the 'apply' decorator does 
      not get passed on to reimplemented methods in subclasses. 
      Implementing inheritance of the accessor decorators seem to require 
      implementation at the metaclass level, which would restrict owner 
      classes to those derived from a particular metaclass.
      <br><br>
      If the intention is to define a getter function later, this error 
      can be suppressed by passing keyword argument 'requireGetter=False' 
      (by default, is True). Similar keyword arguments are available for 
      setter and deleter. """
      raise AttributeError(monoSpace(e))
    if self.__setter_function__ is None and self.__req_set__:
      e = """The requireSetter keyword argument is set to True, but no 
      setter function were found!"""
      raise AttributeError(monoSpace(e))
    if self.__deleter_function__ is None and self.__req_del__:
      e = """The requireDeleter keyword argument is set to True, but no 
      deleter function were found!"""
      raise AttributeError(monoSpace(e))
    return owner

  def __get__(self, instance: Any, owner: type) -> Any:
    """Getter function implementation"""
    if self.__getter_function__ is None:
      e = """Getter function not available!"""
      raise AttributeError(e)
    return self.__getter_function__(maybe(instance, owner))

  def __set__(self, instance: Any, value: Any) -> None:
    """Setter-function implementation"""
    if self.__setter_function__ is None:
      e = """Setter function not available!"""
      raise AttributeError(e)
    return self.__setter_function__(instance, value)

  def __delete__(self, instance: Any) -> None:
    """Deleter-function implementation"""
    if self.__deleter_function__ is None:
      e = """Deleter function not available!"""
      raise AttributeError(e)
    return self.__deleter_function__(instance)

  def __str__(self) -> str:
    """String representation"""
    clsName = self.__class__.__qualname__
    if self.__field_owner__ is None or self.__field_name__ is None:
      return 'Unbound instance of \'%s\'.' % clsName
    ownerName = self.__field_owner__.__qualname__
    selfName = self.__field_name__
    return '%s.%s (%s)' % (ownerName, selfName, clsName)

  def __repr__(self) -> str:
    """Code representation"""
    clsName = self.__class__.__qualname__
    if self.__field_owner__ is None or self.__field_name__ is None:
      argMsg = []
      if self.__default_value__ is not None:
        argMsg.append(str(self.__default_value__))
      kwargs = {}
      if not self.__req_get__:
        argMsg.append('requireGetter=False')
      if self.__req_set__:
        argMsg.append('requireSetter=True')
      if self.__req_del__:
        argMsg.append('requireDeleter=True')
      if not argMsg:
        return '%s()' % clsName
      return '%s(%s)' % (clsName, ', '.join(argMsg))
