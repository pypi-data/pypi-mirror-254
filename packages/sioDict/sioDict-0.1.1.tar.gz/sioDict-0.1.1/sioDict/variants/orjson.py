
from sioDict.base import IoDict
import orjson

class OrjsonDict(IoDict):
    def __init__(self, path: str, *args, **kwargs):
        self.__orjsonOptions = None
        super().__init__(path, *args, **kwargs)

    def load(self):
        with open(self.path, 'r') as f:
            data = orjson.loads(f.read())
            self.update(data)

    def save(self):
        with open(self.path, 'wb') as f:
            f.write(orjson.dumps(self, option=self.__orjsonOptions))
                  
    def touch(self):
        with open(self.path, 'w') as f:
            f.write("{}")
                  
    @property
    def orjsonOptions(self):
        return self.__orjsonOptions
    
    @orjsonOptions.setter
    def orjsonOptions(self, value):
        self.__orjsonOptions = value