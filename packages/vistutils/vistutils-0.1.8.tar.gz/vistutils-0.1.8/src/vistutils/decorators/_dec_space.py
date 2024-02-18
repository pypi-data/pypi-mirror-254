"""DecSpace provides a namespace object class for sue by the DecMeta
class."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.metas import BaseNamespace, Bases


class DecSpace(BaseNamespace):
  """DecSpace provides a namespace object class for sue by the DecMeta
class."""

  def __init__(self, mcls: type, name: str, bases: Bases,
               **kwargs) -> None:
    BaseNamespace.__init__(self, name, bases, **kwargs)
    self.setMetaclass(mcls)
