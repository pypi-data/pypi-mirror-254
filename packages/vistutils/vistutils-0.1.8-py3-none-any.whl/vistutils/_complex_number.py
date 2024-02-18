"""ComplexNumber represents complex numbers. But really, it demonstrates
the use of the Field descriptor class."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from math import atan2
from typing import Optional

from vistutils.fields import Field


class ComplexNumber:
  """ComplexNumber represents complex numbers. But really, it demonstrates
the use of the Field descriptor class."""

  RE = Field()
  IM = Field()
  ARG = Field()

  def __init__(self, *args, **kwargs) -> None:
    self._realPart = args[0]
    self._imaginaryPart = args[1]

  @classmethod
  def clone(cls, *args, **kwargs) -> ComplexNumber:
    """Calls the owner"""
    return cls(*args, **kwargs)

  @RE.GET
  def _getReal(self) -> float:
    """Getter-function for real part"""
    return self._realPart

  @IM.GET
  def _getImaginary(self) -> float:
    """Getter-function for imaginary part"""
    return self._imaginaryPart

  @ARG.GET
  def _getArg(self) -> Optional[float]:
    """Getter-function for argument"""
    return atan2(self.IM, self.RE)

  def __str__(self) -> str:
    """String representation"""
    sign = '+' if self.IM > 0 else '-'
    return '%.3f%s%.3f' % (self.RE, sign, self.IM)
