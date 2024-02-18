"""The ExpandedClass is a metaclass enabling derived classes to define
certain class level behaviours by implementing certain methods. The naming
convention generally is to name the method __class_call__ instead of
__call__ to indicate that the method is the __call__ method, but defined
on the class rather than the instance. These methods should always be
defined as class methods. Those that have existing behaviour will fall back
to it. Those that do not, will now raise AttributeError.

A few of these methods should be left alone or left to programmers with
more imagination than I have.

The following such methods have existing behaviour that would be overwritten.
__class_call__ - defines what happens when the class is called directly.
The default behaviour is to create a new instance of the class.
__class_str__ - Allows the class to define its representation. The default
behaviour is quite ghastly, so this metaclass does implement an
alternative, which simply returns the __qualname__ of the class.
__class_repr__ - Same as above
__class_getattr__ - Allows the class to define what happens when a key is
not recognized as an attribute. By default, it raises AttributeError.
__class_set_name__ - Relevant for inline class creation in the body of
another class. You have more imagination than I, if you find use for this.
__class_init__ - This method allows augmentation of the class that happens
outside the control of the metaclass. It is invoked as the final step in
class creation process, right before the class is passed to a decorator.
Use with care, you can give yourself a really bad time with this one.
__class_getattribute__ - No! Whatever sick ideas you have, don't!

The following methods have no existing behaviour that would be overwritten.
__class_iter__ and __class_next__ - implements class level iteration
__class_getitem__ - This is already available as of python 3.7 lmao
__class_setitem__ - But they forgot to add this
__class_delitem__ - You don't need this

These methods are not possible, as they define the class creation process
itself.
__class_new__ - Would change the __new__ in the metaclass, but if the
class exists, it's the metaclass have already run __new__.
__class_prepare__ - Same as above"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.metas import AbstractMetaclass


class ExpandedMeta(AbstractMetaclass):
  """Metaclass used to create the ExpandedClass"""
  raise NotImplementedError
