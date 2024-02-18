import typing

class ExtOptions:
    raiseOnError = 0x01
    returnClosest = 0x02

def getDeep(
    d : dict, 
    *keys, 
    default = None,
    options : int = 0
):
    if len(keys) == 0:
        return d
    if len(keys) == 1:
        return d.get(keys[0], default)
    
    for key in keys[:-1]:
        if key not in d:
            if options & ExtOptions.raiseOnError:
                raise KeyError(key)
            elif options & ExtOptions.returnClosest:
                return default
            return default
        d = d[key]
    
    
    if options & ExtOptions.raiseOnError:
        raise KeyError(keys[-1])
    elif options & ExtOptions.returnClosest:
        return default
    
    return d.get(keys[-1], default)

def iterTypeMapping(
    keys : typing.List[str] = None,
    mapping  : typing.Union[
        type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
    ] = dict
):
    index = 0
    counter = 0
    while True:
        if index > len(keys) - 1:
            break
        
        if isinstance(mapping, type):
            yield mapping, keys[index]
        elif isinstance(mapping, list) and counter < len(mapping):
            # (dict, 3) (list, 2) yield 3 times dict and 2 times list
            for i in range(mapping[counter][1]):
                yield mapping[counter][0], keys[index]
            counter += 1
        elif isinstance(mapping, dict):
            yield mapping[keys[index]], keys[index]
            
        index += 1
            

def setDeep(
    d : dict, 
    *keysAndValue,
    expandMapping : typing.Union[
        type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
    ] = dict
):
    if len(keysAndValue) == 0:
        return
    
    if len(keysAndValue) == 1:
        raise KeyError("only 1 key passed in, missing value")
    
    if len(keysAndValue) == 2:
        d[keysAndValue[0]] = keysAndValue[1]
        return
    
    target = d
    for stype, key in iterTypeMapping(keysAndValue[:-2], expandMapping):
        if key not in target:
            target[key] = stype()
        target = target[key]
    
    target[keysAndValue[-2]] = keysAndValue[-1]
    
defaultObj = object()

def setDefaultDeep(
    d : dict, 
    *keys,
    default = defaultObj,
    expandMapping : typing.Union[
        type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
    ] = dict
):
    if len(keys) == 0:
        return
    
    if len(keys) == 1:
        d[keys[0]] = keys[0]
        return
    
    target = d
    for stype, key in iterTypeMapping(keys[:-1], expandMapping):
        if key not in target:
            target[key] = stype()
        target = target[key]
    
    if keys[-1] not in target:
        target[keys[-1]] = default

