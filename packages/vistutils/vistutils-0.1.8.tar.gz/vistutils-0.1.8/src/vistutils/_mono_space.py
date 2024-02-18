"""The monoSpace function receives a string and returns it with all
consecutive white spaces replaced by a single space. Only characters that
are recognized as digits, letters or punctuation are included. Include in
the string the following tags to explicitly set new lines or indentations:
  '<br>' for new lines
  '<n: int>' for indentations of 'n' spaces.
  '<tab>' for one tab containing the number of spaces defined at the
  keyword argument 'tab', by default 2."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from string import digits, punctuation, ascii_letters


def _standardOnly(msg: str) -> str:
  """Helper function removing non-standard characters."""
  chars = [c for c in '%s%s%s' % (ascii_letters, digits, punctuation)]
  return ''.join([c for c in msg if c in chars])


def _nonStandardToSpace(msg: str) -> str:
  """Replaces non-standard characters with spaces."""
  chars = [c for c in '%s%s%s' % (ascii_letters, digits, punctuation)]
  return ''.join([c if c in chars else ' ' for c in msg])


def _singleSpace(msg: str) -> str:
  """Replaces all occurrences of multiple spaces with a single space."""
  return _singleSpace(msg.replace('  ', ' ')) if '  ' in msg else msg


def monoSpace(msg: str, **kwargs) -> str:
  """The monoSpace function receives a string and returns it with all
consecutive white spaces replaced by a single space. Only characters that
are recognized as digits, letters or punctuation are included. Include in
the string the following tags to explicitly set new lines or indentations:
  '<br>' for new lines
  '<n: int>' for indentations of 'n' spaces. (Max is 16)
  '<tab>' for one tab containing the number of spaces defined at the
  keyword argument 'tab', by default 2.
  By default, the UNIX style newline character ('\n') is used. Specify
  at keyword argument 'newLineChar' to any string or one of:
  UNIX, WINDOWS, MAC, oldMAC yielding '\n', '\r\n', '\n' or '\r'
  respectively.
  To specify a different newline tag than '<br>' use keyword argument
  newLineTag.
  """

  msg = _nonStandardToSpace(msg)
  msg = _singleSpace(msg)
  tabLength = kwargs.get('tab', 2)
  newLineTag = kwargs.get('newLineTag', '<br>')
  newLineChar = kwargs.get('newLineChar', '\n')
  OSNewLineChar = dict(unix='\n', windows='\r\n', mac='\n', oldmac='\r')
  if newLineChar.lower() in OSNewLineChar:
    newLineChar = OSNewLineChar.get(newLineChar.lower())
  msg = msg.replace(newLineTag, newLineChar)
  msg = msg.replace('<tab>', ' ' * tabLength)
  for i in range(16):
    msg = msg.replace('<%d>' % i, ' ' * i)
  return msg
