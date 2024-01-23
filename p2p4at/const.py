from os import environ
from pathlib import Path

_HOME = Path(environ.get("HOME", ""))
CONFIG_PATH = _HOME / ".config" / "p2p4at" / "config.ini"
DATA_PATH = _HOME / ".local" / "share" / "p2p4at" / "data"
RENDEZVOUS_PORT = 1858
