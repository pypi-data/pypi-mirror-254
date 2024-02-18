import os
from typing import NotRequired, TypedDict
import typing

from sprinko.extra.dictionary import AutoSaveDict

# [appdata]
core_dir = os.path.dirname(os.path.realpath(__file__))
mod_dir = os.path.dirname(core_dir)

appdata_dir= os.path.join(mod_dir, "appdata")

os.makedirs(appdata_dir, exist_ok=True)

# [appdata/caching]
caching_dir = os.path.join(appdata_dir, "caching")

os.makedirs(caching_dir, exist_ok=True)

# [appdata/scenarios.json]
scenarios = AutoSaveDict(os.path.join(appdata_dir, "scenarios.json"))

# [appdata/cfg.json]
cfg = AutoSaveDict(os.path.join(appdata_dir, "cfg.json"))

cfg_config = cfg.ensure_child("config")

# [appdata/bottles.json]
class BottleEntry(TypedDict):
    path : str
    type : typing.Literal["local", "gitraw", "ref"]

bottles : typing.Union[typing.Dict[str, BottleEntry], AutoSaveDict] = cfg.ensure_child("bottles")

# [appdata/caching.json]

class CacheEntry(TypedDict):
    checksum : str
    type : typing.Literal["local", "gitraw"]
    updatableInterval : NotRequired[int]
    lastPulled : NotRequired[str]
    lastCommitted : NotRequired[str]

caching : typing.Union[typing.Dict[str, typing.Union[str, CacheEntry]], AutoSaveDict] = AutoSaveDict(os.path.join(appdata_dir, "caching.json"))
