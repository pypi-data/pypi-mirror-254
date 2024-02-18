"""The stringList function receives a single string describing a list of
items and returns a list of strings each representing an item."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils import monoSpace


def stringList(msg: str, **kwargs) -> list[str]:
  """The stringList function receives a single string describing a list of
items and returns a list of strings each representing an item."""
  separator = kwargs.get('separator', ', ')
  data = monoSpace(msg)
  return [item.strip() for item in data.split(separator)]
