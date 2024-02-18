from sioDict.variants.json import JsonDict

try:
    from warnings import warn as _warn
except ImportError:
    pass

try:
    from sioDict.variants.toml import TomlDict
except ImportError as _TomlDictE:
    def TomlDict(*args, **kwargs):
        global _TomlDictE
        _warn(_TomlDictE)
        
try:
    from sioDict.variants.orjson import OrjsonDict
except ImportError as _OrjsonDictE:
    def OrjsonDict(*args, **kwargs):
        global _OrjsonDictE
        _warn(_OrjsonDictE)
        