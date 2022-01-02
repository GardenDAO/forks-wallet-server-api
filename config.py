import os
from pathlib import Path
from chia.util.default_root import DEFAULT_ROOT_PATH
from chia.util.config import load_config

FORKS = ["xch", "xfl", "xcd", "hdd"]

REDIS_HOST = ''
REDIS_PWD = ''

CHIA_ROOT_PATH = DEFAULT_ROOT_PATH
CHIA_CONFIG = load_config(CHIA_ROOT_PATH, "config.yaml")

# Add other blockchains HERE
# below is not purist, but from a security perspective it's a nice idea to not be loading
# in multiple copies of the code across various forks.
#
# TODO error handling if files don't exist
FLORA_ROOT_PATH = Path(os.path.expanduser(os.getenv("FLORA_ROOT", "~/.flora/mainnet"))).resolve()
FLORA_CONFIG = load_config(FLORA_ROOT_PATH, "config.yaml")

CRYPTODOGE_ROOT_PATH = Path(os.path.expanduser(os.getenv("CRYPTODOGE_ROOT", "~/.cryptodoge/mainnet"))).resolve()
CRYPTODOGE_CONFIG = load_config(CRYPTODOGE_ROOT_PATH, "config.yaml")

HDDCOIN_ROOT_PATH = Path(os.path.expanduser(os.getenv("HDDCOIN_ROOT", "~/.hddcoin/mainnet"))).resolve()
HDDCOIN_CONFIG = load_config(HDDCOIN_ROOT_PATH, "config.yaml")
