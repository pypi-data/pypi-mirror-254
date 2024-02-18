from functools import cache, cached_property
import typing
from typing import Any
import zipfile
from sprinko.base.caching import get_git_cache, get_local_cache
from sprinko.base.env import bottles as bottles_cfg
import io
import toml

class BottleMeta(type):
    _instances : typing.Dict[str, "Bottle"] = {}
    
    def __call__(cls, name : str, addr : str, type_ : typing.Literal["local", "gitraw", "ref"]):
        if name not in cls._instances:
            cls._instances[name] = super(BottleMeta, cls).__call__(name, addr, type_)
        return cls._instances[name]
        
class Bottle(metaclass=BottleMeta):
                
    def __init__(self, name : str, addr : str, type_ : typing.Literal["local", "gitraw", "ref"]):
        self.__addr = addr
        self.__type = type_
        self.__name = name
        
        self.refresh()
        
    @property
    def name(self):
        return self.__name
        
    @property
    def type(self):
        return self.__type
        
    def __getattribute__(self, __name: str) -> Any:
        if __name.startswith("_"):
            return super().__getattribute__(__name)
        elif hasattr(self, f"_Bottle__{self.__type}_{__name}"):
            return getattr(self, f"_Bottle__{self.__type}_{__name}")
        else:
            return super().__getattribute__(__name)
        
    @property
    def addr(self):
        return self.__addr
    
    @classmethod
    def instances(cls, refresh : bool = False):
        if not refresh and len(cls._instances) > 0:
            return cls._instances
        
        instanceVals = cls._instances.values()
        cfgVals = bottles_cfg.values()
        
        instancePaths = [v.addr for v in instanceVals]
        cfgPaths = [v["path"] for v in cfgVals]
       
        pathToName = {p : v for p, v in zip(cfgPaths, bottles_cfg.keys())}
       
        if instancePaths == cfgPaths:
            return cls._instances
        
        #
        pending_to_delete = set(instancePaths) - set(cfgPaths)
        pending_to_add = set(cfgPaths) - set(instancePaths)
    
        for addr in pending_to_delete:
            v = cls._instances.pop(addr)
            del v
        
        for addr in pending_to_add:
            name = pathToName[addr]
            Bottle(name, addr, bottles_cfg[name]["type"])
        
        # intersect
        pending_refresh = set(instancePaths) & set(cfgPaths)
        for path in pending_refresh:
            name = pathToName[path]
            cls._instances[name].refresh()
        
        return cls._instances
    
    def refresh(self, refetch : bool = False):
        if hasattr(self, "__zipCache"):
            self.__zipCache.close()
            del self.__zipCache
            
        self.getScript.cache_clear()
        if self.__type == "gitraw":
            byteData = get_git_cache(f"{self.addr}/bottle.zip", force=refetch)
            self.__zipCache = zipfile.ZipFile(io.BytesIO(byteData)) 
            # split extension
        elif self.__type == "local":
            byteData = get_local_cache(self.addr, force=refetch)
            self.__zipCache = zipfile.ZipFile(io.BytesIO(byteData))
        else:
            raise NotImplementedError
        
    @property
    def scriptlist(self):
        if self.__type in ["gitraw", "local"]:
            return {
                n.split(".")[0] : n for n in self.__zipCache.namelist() 
                if any(n.endswith(x) for x in [".py"])
            }

        raise NotImplementedError("Unimplemented")
        
    def getFile(self, name : str, save : bool = False, saveAs : str = None): 
        if self.__zipCache:
            if save:
                if saveAs is None:
                    saveAs = name
                with open(saveAs, "wb") as sf:
                    sf.write(self.__zipCache.open(name).read())
                return
            else:
                return self.__zipCache.open(name)
            
        raise NotImplementedError("Unimplemented")
    
    @cache
    def getScript(self, name : str):
        if name in self.scriptlist:
            return self.getFile(self.scriptlist[name]).read()
        elif name in self.scriptlist.values():
            return self.getFile(name).read()
        
    @cached_property
    def meta(self):
        file = self.getFile("bottle.toml")
        return toml.loads(file.read().decode("utf-8"))
        
    @cached_property
    def filelist(self):
        return self.__zipCache.namelist()
        
    @classmethod
    def fullMeta(cls):
        instances = cls.instances()
        meta = {}
        for item in instances.values():
            for k, v in item.meta.get("intel", {}).items():
                if k not in meta:
                    meta[k] = v
                elif isinstance(v, list):
                    meta[k].extend(v)
                elif isinstance(v, dict):
                    for k2, v2 in v.items():
                        if k2 not in meta[k]:
                            meta[k][k2] = v2
                            
        return meta
                            
    @classmethod
    def fullscriptlist(cls):
        instances = cls.instances()
        scriptlist = {}
        for item in instances.values():
            scriptlist.update(item.scriptlist)
        return scriptlist
    
    @classmethod
    def fullScripts(cls):
        instances = cls.instances()
        scripts = {}
        for item in instances.values():
            if item.__type in ["gitraw", "local"]:
                scripts.update(item.__zipCache.namelist())
            else:
                raise NotImplementedError("Unimplemented")
        return scripts
                            
    @classmethod
    def unreg(cls, key : str):
        if key not in bottles_cfg:
            raise KeyError(f"Bottle {key} not found")
        
        bottles_cfg.pop(key)
        cls.instances(refresh=True)
        
    @classmethod
    def reg(cls, name : str, addr : str, type_ : typing.Literal["local", "gitraw", "ref"], ignoreExists : bool = False):
        if name in bottles_cfg and not ignoreExists:
            raise KeyError(f"Bottle {name} already exists")
        
        if name not in bottles_cfg:
            bottles_cfg[name] = {"path" : addr, "type" : type_}
        inlist = cls.instances(refresh=True)
        return inlist[name]
                    
        