"""Res subclasses CompletedProcess from the subprocess module exposing its
content in a more flexible manner"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from subprocess import CompletedProcess, PIPE, run
from typing import Optional

from vistutils.fields import Field
from vistutils.waitaminute import ParsingError


class MetaRes(type):
  """Cheeky"""

  def __instancecheck__(cls, instance) -> bool:
    if isinstance(instance, CompletedProcess):
      return True
    return type.__instancecheck__(cls, instance)


class Res(metaclass=MetaRes):
  """Res subclasses CompletedProcess from the subprocess module exposing its
content in a more flexible manner. """

  out = Field()
  err = Field()
  cmd = Field()
  ret = Field()

  @out.GET
  def getOut(self) -> str:
    """Getter-function for stdout"""
    res = self.__completed_process__
    return res.stdout.decode('utf-8')

  @err.GET
  def getErr(self) -> str:
    """Getter-function for stderr"""
    res = self.__completed_process__
    return res.stderr.decode('utf-8')

  @cmd.GET
  def getCmd(self) -> str:
    """Getter-function for stdout"""
    res = self.__completed_process__
    out = res.args
    if isinstance(out, str):
      return out
    if isinstance(out, bytes):
      return out.decode('utf-8')
    if isinstance(out, (list, tuple)):
      out = [*out, ]
    out2 = []
    for arg in out:
      if isinstance(arg, str):
        out2.append(arg)
      if isinstance(arg, bytes):
        out2.append(arg.decode('utf-8'))
    return ' '.join(out2)

  @ret.GET
  def getRet(self) -> int:
    """Getter-function for stdout"""
    res = self.__completed_process__
    return int(res.returncode)

  @staticmethod
  def parseCommands(*args, ) -> Optional[CompletedProcess]:
    """Parses arguments to commands, runs them and returns the results"""
    strArgs = []
    for arg in args:
      if isinstance(arg, str):
        strArgs.append(arg)
      elif isinstance(arg, bytes):
        strArgs.append(arg.decode('utf-8'))
    cmd = ' '.join([arg for arg in args if isinstance(arg, str)])
    if cmd:
      return run(cmd, shell=True, stdout=PIPE, stderr=PIPE)

  @staticmethod
  def parseCompletedProcess(*args, ) -> Optional[CompletedProcess]:
    """Searches arguments for instance of completed process"""
    for arg in args:
      if isinstance(arg, CompletedProcess):
        return arg

  @classmethod
  def parseArgs(cls, *args) -> Optional[CompletedProcess]:
    """Parses positional arguments"""
    res = None
    for parse in [cls.parseCompletedProcess, cls.parseCommands]:
      res = parse(*args)
      if res is not None:
        if isinstance(res, CompletedProcess):
          return res
    e = """Unable to parse positional arguments to commands or completed 
    process!"""
    raise ParsingError(e)

  def __init__(self, *args, **kwargs) -> None:
    self.__completed_process__ = self.parseArgs(*args)

  def __int__(self, ) -> int:
    """Return code"""
    return self.__completed_process__.returncode

  def __str__(self, ) -> str:
    """String representation"""
    if not int(self):
      return self.out
