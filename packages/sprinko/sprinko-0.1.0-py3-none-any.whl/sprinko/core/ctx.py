from types import MappingProxyType
import typing


class CtxMeta(type):
    _singleton : object= None
    
    def __call__(cls, *args, **kwargs):
        if cls._singleton and not isinstance(cls._singleton, cls):
            raise ValueError(f"There already exists a singleton of {cls._singleton.__class__}")

        if not cls._singleton:
            cls._singleton = super(CtxMeta, cls).__call__(*args, **kwargs)

        return cls._singleton

class CtxInfo:
    def __init__(self):
        self.__currentKey = None
        self.__currentSeq = 0
        self.__runSequence = list()
    
    @property
    def currentKey(self) -> str:
        return self.__currentKey
    
    @property
    def currentSeq(self) -> int:
        return self.__currentSeq
    
    @property
    def runSequence(self) -> typing.List[str]:
        return list(self.__runSequence)

    @property
    def lastKey(self) -> str:
        return self.__runSequence[-1]
    

class CtxBase(metaclass=CtxMeta):
    def __init__(self):
        self.__data = dict()
        self.__data["ctx"] = self
        self.__info = CtxInfo()
        self.__scoped = dict()
    
    @property
    def info(self) -> CtxInfo:
        return self.__info
    
    @property
    def data(self) -> MappingProxyType:
        return MappingProxyType(self.__data)

    def get(self, key : str, default = None):
        return self.__data.get(key, default)
    
    def set(self, __d : dict = None, key : typing.Union[str, tuple] = None, **kwargs):
        if isinstance(key, tuple):
            if not key:
                key = None
            elif len(key) == 1:
                key = key[0]
        
        if key is None:
            target = self.__data
        if key not in self.__scoped:
            self.__scoped[key] = dict()
            target : dict = self.__scoped[key]
        else:
            target : dict = self.__scoped[key]
        
        if __d is not None:
            target.update(__d)
        target.update(kwargs)
        
    def __getAllDictThatContains(self, key : str):
        ret = {}
        for k, v in self.__scoped.items():
            if isinstance(k, str) and k == key:
                ret.update(v)
            elif isinstance(k, tuple) and key in k:
                ret.update(v)
        
        return ret
    
    def __generateAdded(self, contained : dict):
        return set(contained.keys()) - set(self.__data.keys())
    
    def __generateModified(self, contained : dict):
        res = []
        for k, v in contained.items():
            if k in self.__data and v != self.__data[k]:
                res.append(k)
        
        return res
        
    def push(self, key : str):
        self.__info._CtxInfo__currentKey = key
        self.__info._CtxInfo__currentSeq += 1
        
        contained = self.__getAllDictThatContains(key)
        self.__newlyAdded = self.__generateAdded(contained)
        self.__newlyModified = self.__generateModified(contained)
        
        self.__data.update(contained)
        
    def pop(self):
        self.__info._CtxInfo__runSequence.append(self.info.currentKey)
        
    def expose(self):
        return self.__data
    
    def getScope(self, key : str, scopeOnly : bool = True):
        contained = self.__getAllDictThatContains(key)
        if scopeOnly:
            return contained
        copied = self.__data.copy()
        copied.update(contained)
        return copied
    
    
    
class Ctx(CtxBase):
    pass