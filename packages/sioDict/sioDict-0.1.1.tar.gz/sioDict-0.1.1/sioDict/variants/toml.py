
from sioDict.base import IoDict
import toml

class TomlDict(IoDict):

    def load(self):
        data = toml.load(self.path)
        self.update(data)

    def save(self):
        with open(self.path, 'wb') as f:
            toml.dump(self, f)
                  
    def touch(self):
        with open(self.path, 'a'):
            pass
                  