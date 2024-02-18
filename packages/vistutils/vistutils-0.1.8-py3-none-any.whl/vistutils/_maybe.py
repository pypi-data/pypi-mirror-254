"""The maybe function and related functions provide None-aware type
filtering."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from builtins import tuple
from typing import Any, Optional, Union

Types = Union[type, list[type], tuple[type, ...]]
Number = Union[Union[int, float, complex]]
Ints = Union[int, tuple[int, ...], list[int]]
Floats = Union[float, tuple[float, ...], list[float]]
Complexes = Union[complex, tuple[complex, ...], list[complex]]


def maybe(*args, ) -> Any:
  """Returns the first positional argument that is different from None"""
  for arg in args:
    if arg is not None:
      return arg


def _collectTypes(*args, ) -> tuple[Types, list]:
  """Splits the positional arguments into types and non-types. Types must
be the first positional arguments."""
  type_ = []
  for arg in args:
    if isinstance(arg, type):
      type_.append(arg)
    else:
      break
  return type_, [arg for arg in args if arg not in type_]


def _floatInt(intCandidate: float) -> Optional[int]:
  """Tries to cast the given float as an integer."""
  if (intCandidate - round(intCandidate)) ** 2 < 1e-06:
    return int(round(intCandidate))


def _complexFloat(floatCandidate: complex) -> Optional[float]:
  """Tries to cast the given complex as a float."""
  if floatCandidate.imag ** 2 < 1e-06:
    return floatCandidate.real
  if floatCandidate.real ** 2 < 1e-06:
    return floatCandidate.imag


def _maybeInt(*args, **kwargs) -> Optional[Ints]:
  """Tries to find either the first or all arguments of integer type.
Arguments of float or complex are valid, if they are near an integer. In
this case that integer replaces it."""
  out = []
  for arg in args:
    if isinstance(arg, int):
      out.append(arg)
    elif isinstance(arg, float):
      val = _floatInt(arg)
      if isinstance(val, int):
        out.append(val)
    elif isinstance(arg, complex):
      val = _complexFloat(arg)
      if isinstance(val, float):
        val2 = _floatInt(val)
        if isinstance(val2, int):
          out.append(val2)
    if out and not kwargs.get('all', False):
      return out[0]
  if out:
    return out


def _maybeFloat(*args, **kwargs) -> Optional[Floats]:
  """Tires to find either the first or all arguments of float type.
Arguments of complex type are valid, if either their real or imaginary
part is near zero. """
  out = []
  for arg in args:
    if isinstance(arg, int):
      out.append(float(1.0 * arg))
    elif isinstance(arg, float):
      out.append(arg)
    elif isinstance(arg, complex):
      val = _complexFloat(arg)
      if isinstance(val, float):
        out.append(val)
    if out and not kwargs.get('all', False):
      return out[0]
  if out:
    return out


def _maybeComplex(*args, **kwargs) -> Optional[Complexes]:
  """Tires to find either the first or all arguments of complex type."""
  out = []
  for arg in args:
    if isinstance(arg, int):
      out.append(float(arg) + 0.0j)
    elif isinstance(arg, float):
      out.append(arg + 0.0j)
    elif isinstance(arg, complex):
      out.append(arg)
    if out and not kwargs.get('all', False):
      return out[0]
  if out:
    return out


def maybeType(*args, ) -> Any:
  """Returns the first positional argument belonging to given type"""
  types, args = _collectTypes(*args, )
  for type_ in types:
    if type_ is int:
      return _maybeInt(*args, all=False)
    if type_ is float:
      return _maybeFloat(*args, all=False)
    if type_ is complex:
      return _maybeComplex(*args, all=False)
    for arg in args:
      if isinstance(arg, type_):
        return arg


def maybeTypes(*args, ) -> Any:
  """Returns the all positional arguments belonging to a given type."""
  types, args = _collectTypes(*args, )
  out = []
  for type_ in types:
    if type_ is int:
      out.extend(_maybeInt(*args, all=True))
    elif type_ is float:
      out.extend(_maybeFloat(*args, all=True))
    elif type_ is complex:
      out.extend(_maybeComplex(*args, all=True))
    else:
      for arg in args:
        if isinstance(arg, type_):
          out.append(arg)
  return out
