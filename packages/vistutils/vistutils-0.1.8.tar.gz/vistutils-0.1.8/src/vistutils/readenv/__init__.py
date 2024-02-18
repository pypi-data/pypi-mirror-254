"""The readenv module provides functionality required for reading .env
files. The module assumes that the root folder may be identified by
containing files: LICENSE, README.md and .env.example."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ._read_env_exception import ReadEnvException
from ._get_parent import getParent
from ._get_root import getRoot
from ._read_file import readFile
from ._load_env import loadEnv
from ._parse_env import parseEnv
from ._apply_env import applyEnv
