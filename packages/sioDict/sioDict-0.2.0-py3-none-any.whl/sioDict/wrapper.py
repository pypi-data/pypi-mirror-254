
import abc
from contextlib import contextmanager
import typing
from sioDict.base import SioBase
from sioDict.etc import ExtOptions, getDeep, setDeep, setDeepSimple
import orjson

class SioWrapper:
    def __init__(
        self, 
        path : str, 
        *args, 
        reset : bool = False,
        **kwargs
    ):
        self.__base = SioBase(*args, **kwargs)
        self.__base.loadMethod = self._load
        self.__base.saveMethod = self._save
        self.__base.clearMethod = self._clear
        self.__base.syncFile(path, reset)
        
    @abc.abstractstaticmethod
    def _load(path : str):
        with open(path, 'rb') as f:
            return orjson.loads(f.read())
    
    @abc.abstractstaticmethod
    def _save(d, path : str):
        with open(path, 'wb') as f:
            f.write(orjson.dumps(d))
    
    @abc.abstractstaticmethod
    def _clear(path : str):
        with open(path, 'w') as f:
            f.write("{}")

    @property
    def _internalBase(self):
        return self.__base

    def __setitem__(self, keys, val):
        with self.saveLock():
            keys = keys if isinstance(keys, tuple) else [keys]

            return setDeepSimple(self.__base, *keys, val)

    def __getitem__(self, keys):
        keys = keys if isinstance(keys, tuple) else [keys]
        return getDeep(self.__base, *keys, options=ExtOptions.raiseOnError)

    @contextmanager
    def saveLock(self, saveAfter : bool = True):
        yield self.__base.saveLock(saveAfter)

    def pop(self, key):
        return self.__base.pop(key)
    
    def popitem(self):
        return self.__base.popitem()
    
    def __delitem__(self, key):
        with self.saveLock():
            self.__base.__delitem__(key)

    def update(self, *args, **kwargs):
        with self.saveLock():
            self.__base.update(*args, **kwargs)


    #ANCHOR misc
    def setDeep(
        self,
        *keysAndValue,
        expandMapping : typing.Union[
            type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
        ] = dict
    ):
        with self.saveLock():
            setDeep(self.__base, *keysAndValue, expandMapping=expandMapping)

    def getDeep(
        self,
        *keys,
        default = None,
        options : int = 0
    ):
        return getDeep(self.__base, *keys, default=default, options=options)
    

    #ANCHOR dict methods
    def get(self, key, default = None):
        return self.__base.get(key, default)
    
    def __contains__(self, key):
        return self.__base.__contains__(key)

    def items(self):
        return self.__base.items()
    
    def keys(self):
        return self.__base.keys()
    
    def values(self):
        return self.__base.values()
    
    def clear(self):
        with self.saveLock():
            self.__base.clear()

    def __len__(self):
        return self.__base.__len__()
    
    def __iter__(self):
        return self.__base.__iter__()
    
    def __str__(self):
        return str(self.__base)
    
    def __repr__(self):
        return repr(self.__base)
    
    def __eq__(self, other):
        return self.__base == other
    
    def __ne__(self, other):
        return self.__base != other
    
    