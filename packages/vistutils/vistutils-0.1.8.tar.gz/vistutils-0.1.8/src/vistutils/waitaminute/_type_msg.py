"""The typeMsg module creates a standardized message for type errors where
an object as an unexpected type. The function takes as arguments:

name: The name of the object as it was referred to in the scope
actObj: The actual object received
actType: The actual type of the object
expType: The expected type of the object

"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any


def typeMsg(name: str, actObj: Any, expType: type) -> str:
  """The typeMsg module creates a standardized message for type errors where
an object as an unexpected type. The function takes as arguments:

name: The name of the object as it was referred to in the scope
actObj: The actual object received
actType: The actual type of the object
expType: The expected type of the object

"""
  actStr = str(actObj)
  actTypeName = type(actObj).__qualname__
  expTypeName = expType.__qualname__
  e = """Expected object at name: '%s' to be of type '%s' but received 
  '%s' of type: '%s'!"""
  return e % (name, actTypeName, actStr, expTypeName)
