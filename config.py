import os
import logging
from pathlib import Path
from chia.util.default_root import DEFAULT_ROOT_PATH
from chia.util.config import load_config

REDIS_HOST = ''
REDIS_PWD = ''

# list of forks supported by ticker symbol
#FORKS = ["xch", "xfl", "xcd", "hdd"] 
FORKS = ["xch", "hdd"] #
DEFAULT_ROOTS = { 'xch': { 'env': "DEFAULT_ROOT_PATH", 'dir': "~/.chia/mainnet" },
    'xfl': { 'env': "FLORA_ROOT", 'dir': "~/.flora/mainnet" },
    'xcd': { 'env': "CRYPTODOGE_ROOT", 'dir': "~/.cryptodoge/mainnet" },
    'hdd': { 'env': "HDDCOIN_ROOT", 'dir': "~/.hddcoin/mainnet" },
    }

ROOT_PATH = {} # array of the root paths of where each fork's config files are
CHAIN_CONFIG = {} # array of the configs for each fork
for fork in FORKS:
    ROOT_PATH[fork] = Path(os.path.expanduser(os.getenv(DEFAULT_ROOTS[fork]['env'], DEFAULT_ROOTS[fork]['dir']))).resolve()
    #logging.warning(ROOT_PATH[fork])
    CHAIN_CONFIG[fork] = load_config(ROOT_PATH[fork], "config.yaml")
