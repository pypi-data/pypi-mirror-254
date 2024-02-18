"""EffortException is raised were functionality would logically be expected
but where the effort required for implementation substantially exceeds any
benefit or utility."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


class EffortException(Exception):
  """EffortException is raised were functionality would logically be expected
but where the effort required for implementation substantially exceeds any
benefit or utility."""

  def __init__(self, *args, **kwargs) -> None:
    Exception.__init__(self, *args)
