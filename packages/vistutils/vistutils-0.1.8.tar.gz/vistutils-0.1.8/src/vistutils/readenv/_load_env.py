"""The load  function locates the environment file, reads the contents and
inserts them as environment variables. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from vistutils.readenv import getRoot, readFile, ReadEnvException


def loadEnv(**kwargs) -> list[str]:
  """The load  function locates the environment file, reads the contents and
inserts them as environment variables. """

  lines = None

  there = getRoot()
  env_file = os.path.join(there, '.env')
  env_example_file = os.path.join(there, '.env.example')

  if os.path.exists(env_file):
    if os.path.isfile(env_file):
      lines = readFile(env_file)

  if lines is None:
    if os.path.exists(env_example_file):
      if os.path.isfile(env_example_file):
        lines = readFile(env_example_file)

  if lines is None:
    e = """Failed to locate environment file .env or .env.example."""
    raise ReadEnvException(e)

  return lines
