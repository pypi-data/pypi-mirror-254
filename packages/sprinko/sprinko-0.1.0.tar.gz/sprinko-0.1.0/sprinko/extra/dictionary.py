from contextlib import contextmanager
import os
import shutil
import typing
import orjson

ERROR = object()

def getDeep(d, *args):
    """
    Get the deeply nested value from the given dictionary using the provided keys or indices.
    :param d: The dictionary to extract the value from.
    :param args: The keys or indices to traverse the nested structure.
    :return: The extracted value, or 'ERROR' if an exception is encountered.
    """
    try:
        target = d
        for arg in args:
            match target:
                case dict():
                    target = target[arg]
                case list():
                    target = target[int(arg)]
                case _:
                    target = getattr(target, arg)
                    
        return target
    except: # NOQA
        return ERROR


def setDeep(d, *args, usingType : typing.Type[dict] = dict):
    """
    Sets a value deeply in a nested dictionary.

    Args:
        d: The input dictionary.
        *args: A sequence of keys to traverse the nested dictionary.
        usingType: The type of the nested dictionary, default is dict.

    Returns:
        None
    """
    if len(args) == 0:
        return
    
    for arg in args[:-2]:
        if arg not in d:
            d[arg] = usingType()
        d = d[arg]

    d[args[-2]] = args[-1]

class _Shared(dict):
    def ensure_child(self, *args) -> 'AutoSaveDictChild':
        target = self
        for arg in args[:-1]:
            if arg not in target:
                target[arg] = dict()
            target = target[arg]
            
        if args[-1] not in target:
            target[args[-1]] = AutoSaveDictChild(self)
        else:
            target[args[-1]] = AutoSaveDictChild(self, target[args[-1]])
        
        return target[args[-1]]
        
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save()

    def __delitem__(self, key):
        super().__delitem__(key)
        self._save()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self._save()

    def clear(self):
        super().clear()
        self._save()

    def pop(self, *args):
        result = super().pop(*args)
        self._save()
        return result

    def popitem(self):
        result = super().popitem()
        self._save()
        return result

    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default
        return self[key]
    
    def setDeep(self, *args, usingType : typing.Type[dict] = dict):
        setDeep(self, *args, usingType = usingType)
        self._save()
        
    def getDeep(self, *args):
        """
        Method to get deep with the given arguments.
        """
        return getDeep(self, *args)
    
    def setDefaultDeep(self, *args):
        """
        Set the default value for a given parameter deep in the object.
        
        Args:
            *args: Variable number of arguments to specify the parameter and its value.

        Returns:
            None
        """
        res = self.getDeep(*args[:-1])
        if res is ERROR:
            self.setDeep(*args)
            self._save()    
            
    def ensure_type(self, *args, type_: typing.Type[dict], baseType=dict):
        """
        Ensure the type of the given item and set it deep in the dictionary.

        Args:
            *args: Variable length argument list.
            type_: The type to ensure for the item.
            baseType: The base type to use for the item.

        Returns:
            The item set deep in the dictionary.
        """
        # Check if the item already exists and is of the correct type.
        existing_item = self.getDeep(*args)
        if existing_item is not ERROR and isinstance(existing_item, type_):
            return existing_item

        item = type_()

        self.setDeep(*args, item, usingType=baseType)

        return self.getDeep(*args)



class AutoSaveDict(_Shared):
    def __init__(self, filepath, *args, bkup : bool = False, **kwargs):
        self.filepath = filepath
        self.__saveLock = False
        self.__bkup = bkup
        super().__init__(*args, **kwargs)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                f.write('{}')
        try:
            self._load()
        except: # noqa
            raise RuntimeError("Failed to load AutoSaveDict")
    
    @property
    def saveToggle(self):
        return self.__saveLock
    
    @saveToggle.setter
    def saveToggle(self, value):
        self.__saveLock = value
        
    @contextmanager
    def saveLock(self, runSaveOnExit = True):
        self.saveToggle = True
        yield
        self.saveToggle = False
        if runSaveOnExit:
            self._save()
    
    def _save(self):
        if self.__saveLock:
            return
        
        if self.__bkup and os.path.exists(self.filepath):
            shutil.copyfile(self.filepath, os.path.join(os.path.dirname(self.filepath), f"{os.path.basename(self.filepath)}.bkup"))
        
        with open(self.filepath, 'wb') as f:
            f.write(orjson.dumps(self, option=orjson.OPT_SERIALIZE_NUMPY | orjson.OPT_INDENT_2 | orjson.OPT_UTC_Z))
            
    def _load(self):
        with open(self.filepath, 'rb') as f:
            self.update(orjson.loads(f.read()))
            
        
class AutoSaveDictChild(_Shared):
    """
    This class represents a child of AutoSaveDict with automatic saving capabilities.

    Methods:
    - __init__(self, parent: AutoSaveDict, *args, **kwargs): Initializes the class with a reference to the parent AutoSaveDict, a reference dictionary, and a save lock.
    - saveToggle: Getter method for the save lock.
    - saveToggle: Setter method for the save lock.
    - saveLock(self, runSaveOnExit=True): Context manager that toggles the save lock and triggers save on exit.
    - _save(self): Triggers save on the parent AutoSaveDict.
    - __getitem__(self, __key): Overrides the dictionary get method to handle missing keys by setting them from the reference dictionary.
    - __setitem__(self, key, value): Overrides the dictionary set method to handle setting keys not present in the reference dictionary.
    - setReference(self, referenceDict): Sets the reference dictionary for the class.
    """
    def __init__(self, parent : AutoSaveDict, *args, **kwargs):
        self.parent = parent
        self.__referenceDict = None
        self.__saveLock = False
        super().__init__(*args, **kwargs)
        
    @property
    def saveToggle(self):
        return self.__saveLock
    
    @saveToggle.setter
    def saveToggle(self, value):
        self.__saveLock = value
        
    @contextmanager
    def saveLock(self, runSaveOnExit = True):
        self.saveToggle = True
        yield
        self.saveToggle = False
        if runSaveOnExit:
            self._save()
    
    def _save(self):
        self.parent._save()
    
    def __getitem__(self, __key):
        if self.__referenceDict is not None and __key not in self.__referenceDict:
            raise KeyError(__key)
        
        if __key not in self:
            self[__key] = self.__referenceDict[__key]
            
        return super().__getitem__(__key)
        
    def __setitem__(self, key, value):
        if self.__referenceDict is not None and key not in self.__referenceDict:
            raise KeyError(key)
        
        return super().__setitem__(key, value)    
    
    def setReference(self, referenceDict):
        self.__referenceDict = referenceDict
        
__all__ = [
    "AutoSaveDict", "AutoSaveDictChild",
    "setDeep", "getDeep",
    "ERROR"
]