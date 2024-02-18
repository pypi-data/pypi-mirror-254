
from sioDict.base import IoDict
import json

class JsonDict(IoDict):
    def load(self):
        with open(self.path, 'r') as f:
            data = json.load(f)
            self.update(data)

    def save(self):
        with open(self.path, 'wb') as f:
            json.dump(self, f, indent=4)
                  
    def touch(self):
        with open(self.path, 'w') as f:
            f.write("{}")
                  