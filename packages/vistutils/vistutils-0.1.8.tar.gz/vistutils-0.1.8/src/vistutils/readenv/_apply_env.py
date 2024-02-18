"""The applyEnv function locates environment file .env or .env.example,
reads the lines in the file, collects them to a dictionary and finally
assigns the key-value pairs as environment variables."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
from typing import Optional

from vistutils.readenv import loadEnv, parseEnv
from vistutils import monoSpace


def applyEnv(**kwargs) -> Optional[list[dict[str, str]]]:
  """The applyEnv function locates environment file .env or .env.example,
reads the lines in the file, collects them to a dictionary and finally
assigns the key-value pairs as environment variables."""
  lines = loadEnv()
  data = parseEnv(*lines)
  updated = []
  for (key, newVal) in data.items():
    oldVal = os.environ.get(key, None)
    if newVal != oldVal:
      os.environ[key] = newVal
    updated.append(dict(key=key, oldVal=oldVal, newVal=newVal))
  if kwargs.get('verbose', False):
    for item in updated:
      msg = """Updated environment variable <'%s'> from <'%s'> to <'%s'>"""
      print(monoSpace(
        msg % (item['key'], item['oldVal'], item['newVal'])))
  if kwargs.get('return', False):
    return updated
