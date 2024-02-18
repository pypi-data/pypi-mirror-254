"""
The vistutils module collects common modules used across projects
developed by Asger Jon Vistisen.
"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ._get_project_root import getProjectRoot
from ._search_key import searchKey
from ._maybe import maybe, maybeType, maybeTypes
from ._mono_space import monoSpace
from ._string_list import stringList
from .readenv import applyEnv
from ._cat import Cat, CatMeta, CatSpace, CatField
from ._weekday import Weekday
from ._complex_number import ComplexNumber
