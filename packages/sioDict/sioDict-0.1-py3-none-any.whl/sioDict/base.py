
from contextlib import contextmanager
import os
import typing
from sioDict.ext import getDeep, setDeep, setDefaultDeep

class IoDictT(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @contextmanager
    def saveLock(self, saveAfter : bool = True):
        raise NotImplementedError
    
    @property
    def __ref(self):
        if isinstance(self, IoDictChild):
            return self._IoDictChild__parent
        else:
            return self
    
    def __setitem__(self, key, value):
        with self.saveLock():
            if isinstance(value, dict):
                value = IoDictChild(self.__ref, value)  # Convert dict to AChild before assignment
            super().__setitem__(key, value)

    def update(self, *args, **kwargs):
        with self.saveLock():
            for arg in args:
                if isinstance(arg, dict):
                    super().update(arg)
            
            for key, value in kwargs.items():
                if isinstance(value, dict):
                    value = IoDictChild(self.__ref, value)  # Convert dict to AChild before assignment
                super().__setitem__(key, value)
    
    def save(self):
        raise NotImplementedError
    
    def clear(self):
        with self.saveLock():
            super().clear()
            
    def getDeep(
        self, 
        *keys, 
        default = None,
        options : int = 0
    ):
        return getDeep(self, *keys, default = default, options = options)
            
    def setDeep(
        self, 
        *keys, 
        default = None,
        expandMapping : typing.Union[
            type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
        ] = dict
    ):
        return setDeep(self, *keys, default = default, expandMapping = expandMapping)

    def setDefaultDeep(
        self, 
        *keys,
        default = None,
        expandMapping : typing.Union[
            type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
        ] = dict
    ):
        return setDefaultDeep(self, *keys, default = default, expandMapping = expandMapping)
            
class IoDict(IoDictT):
    @contextmanager
    def saveLock(self, saveAfter : bool = True):
        if self.__saveLock:
            yield
            return
        self.__saveLock = True
        yield
        self.__saveLock = False
        if saveAfter:
            self.save()
    
    def __init__(self, path : str, *args, **kwargs):
        super().__init__()
        self.__path = path
        self.__saveLock = False
        
        if not os.path.isfile(path):
            self.touch()
    
        with self.saveLock():
            self.update(*args, **kwargs)
            if os.path.exists(self.path):
                self.load()
        
    @property
    def saveLockStatus(self):
        return self.__saveLock
        
    @property
    def path(self):
        return self.__path
    
    def load(self):
        raise NotImplementedError
    
    def touch(self):
        raise NotImplementedError
    
    def save(self):
        raise NotImplementedError
    
    @property
    def __ref(self):
        return self

class IoDictChild(IoDictT):
    def __init__(self, parent, *args, **kwargs):
        super().__init__()
        self.__parent : IoDict = parent
        self.update(*args, **kwargs)
        
    @property
    def __ref(self):
        return self.__parent
    
    def save(self):
        self.__parent.save()    
    
    @contextmanager
    def saveLock(self, saveAfter : bool = True):
        if self.__parent.saveLockStatus:
            yield
            return
        self.__parent._IoDict__saveLock = True
        yield
        self.__parent._IoDict__saveLock = False
        if saveAfter:
            self.save()