"""The AbstractDispatcher provides an abstract baseclass for class
decorators allowing decorated classes to run in external terminals. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
from abc import abstractmethod
from time import ctime
from typing import Any

from vistutils import monoSpace
from vistutils.decorators import AbstractDecorator
from vistutils.dispatcher import Res

from typing import Union, List

COMMANDS = Union[str, List[str]]


class AbstractDispatcher(AbstractDecorator):
  """The AbstractDispatcher provides an abstract baseclass for class
decorators allowing decorated classes to run in external terminals. """

  def __init__(self, *args, **kwargs) -> None:
    AbstractDecorator.__init__(self, *args, **kwargs)
    self.__temp_file__ = None
    self.__temp_hash__ = None

  def _validateDir(self, tempDir: str = None, **kwargs) -> str:
    """Returns the validated directory or raises an error. """
    tempDir = self._getTempDir() if tempDir is None else tempDir
    if os.path.exists(tempDir):
      if os.path.isfile(tempDir):
        e = """Expected temporary directory but received: '%s' which is a 
        file!"""
        raise NotADirectoryError(monoSpace(e % tempDir))
      return tempDir
    elif kwargs.get('_recursion', False):
      raise RecursionError
    else:
      try:
        os.makedirs(tempDir, )
      except PermissionError as permissionError:
        e = """Failed to create a new directory at '%s', because of: 
        <br>'%s''"""
        pe = str(permissionError)
        raise PermissionError(monoSpace(e % (tempDir, pe)))
      return self._validateDir(tempDir, _recursion=True)

  def _validatePath(self, **kwargs) -> str:
    """Validates file path"""
    tempDir = self._validateDir()
    tempName = self._getTempName()
    tempPath = os.path.join(tempDir, tempName)
    if os.path.exists(tempPath):
      if os.path.isfile(tempPath):
        return tempPath
      e = """The given path: '%s' specifies a directory not a file!"""
      raise IsADirectoryError(monoSpace(e % tempPath))
    return tempPath

  def _receiveInner(self, obj: Any) -> None:
    """Reimplementation"""
    self._setInnerObject(obj)
    tempCode = self._getTempCode(obj)
    tempPath = self._validatePath()
    with open(tempPath, 'w') as f:
      f.write(tempCode)
    self.__inner_object__ = obj

  @classmethod
  @abstractmethod
  def _getTempDir(cls) -> str:
    """Subclasses must implement this method to specify the directory to
which temp script files are saved."""

  @abstractmethod
  def _getTempName(self) -> str:
    """Subclass must implement this method to specify the naming scheme
for the temp file name. """

  @classmethod
  @abstractmethod
  def _getMainCode(cls) -> str:
    """Subclasses must implement this method specifying the contents at
the end of the file in the __name__ == '__main__' conditional."""

  def _getTempCode(self, obj: Any) -> str:
    """Reads and parses the code that would create given object"""
    fid = sys.modules[obj.__module__].__file__
    indentation = os.environ.get('INDENTATION', '  ')
    clsName = self.__class__.__name__

    with open(fid, 'r', encoding='utf-8') as f:
      lines = f.readlines()

    codeLines = [self.getHashbang(), self.getTempComment(), ]
    importLines = self.getImports()
    for line in importLines:
      codeLines.append(line)
    for line in lines:
      if line.strip().startswith('#'):
        pass
      elif line.strip().startswith('@') and '@%s' % clsName in line:
        pass
      else:
        codeLines.append(line)

    nameEqualMain = """if __name__ == '__main__':"""
    codeLines.append(nameEqualMain)
    mainCode = self._getMainCode()
    print(self.__class__.__qualname__)
    print(mainCode)
    mainLines = [line.strip() for line in self._getMainCode()] or [

      'pass']
    for line in mainLines:
      codeLines.append('%s%s' % (indentation, line))
    out = []
    for line in codeLines:
      if isinstance(line, list):
        out.append('\n'.join(line))
      else:
        out.append(line)
    return '\n'.join(out)

  @classmethod
  def getHashbang(cls) -> str:
    """Getter-function for the hashbang to be placed at the top of the
temp file. This defaults to: #!/usr/bin/env python3"""
    return '#!/usr/bin/env python3'

  @classmethod
  def getImports(cls) -> List[str]:
    """Getter-function for implicit import statements that are needed in
the dispatched temp file, but not in the 'real' file."""
    return []

  @classmethod
  def getTempComment(cls) -> List[str]:
    """AbstractDispatchers will create temporary python files. These files
begin with a hashbang following by a comment returned by this method.
By default, mentions the name of the class and nothing else:"""
    maxLineLength = os.environ.get('MAX_LINE_LENGTH', 77)
    msg = """AUTO-CREATED TEMP FILE\nCreated by class: '%s' on '%s'"""
    comment = msg % (cls.__qualname__, ctime())
    comments = monoSpace(comment).split(' ')
    line = '#>-'
    lines = []
    while comments:
      while len(line) + len(comments[0]) + 1 < maxLineLength - 3:
        line = '%s %s' % (line, comments.pop(0))
        if not comments:
          break
      lines.append('%s-<#' % line)
      line = '#>-'
    if line != '#>-':
      lines.append('%s-<#' % line)
    header, footer = '#/', '#\\'
    while len(header) < maxLineLength - 2:
      header = '%s%s' % (header, '¨')
    header = '%s%s' % (header, footer[:2])
    while len(footer) < maxLineLength - 2:
      footer = '%s%s' % (footer, '¨')
    footer = '%s%s' % (footer, header[:2])
    lines = [header, *lines, footer]
    return [header, *lines, footer]

  @classmethod
  @abstractmethod
  def terminal(cls, *args, **kwargs) -> COMMANDS:
    """Subclasses must implement this method to define the terminal
commands that will invoke the dispatch script. The return value should
be a list of commands. Each command can be a string or a new list of
strings. These are then dispatched one at a time consecutively."""

  def run(self, *args, **kwargs) -> List[Res]:
    """This method actually runs the dispatched script"""
    out = []
    for line in self.terminal():
      line = [line, ] if isinstance(line, str) else line
      out.append(Res(*line))
    return out
