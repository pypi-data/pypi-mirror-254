"""The parseEnv function receives the lines from an .env file and returns
a dictionary of environment variables."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


def _includeLine(line: str) -> bool:
  """Decides if line is to be included. If it begins with # or does not
include an equal sign, it is not to be included."""
  return False if line.startswith('#') else True if '=' in line else False


def _parseLine(line: str) -> tuple[str, str]:
  """The _parseLine function receives a line from an .env file and returns
a tuple of the key and value."""
  for (i, char) in enumerate(line):
    if char == '=':
      return line[:i].strip(), line[i + 1:].strip()


def parseEnv(*lines) -> dict:
  """The parseEnv function receives the lines from an .env file and returns
a dictionary of environment variables."""
  data = {}
  included = [line for line in lines if _includeLine(line)]
  for (key, val) in [_parseLine(line) for line in included]:
    data = {**data, **{key: val}}
  return data
