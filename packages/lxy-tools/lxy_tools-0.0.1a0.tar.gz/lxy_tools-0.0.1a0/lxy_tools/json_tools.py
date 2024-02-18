import json
from typing import Any


def json_load(path: str, byte: bool=False) -> Any:
    '''
        json.load() that saves the open() wrapper 
    '''
    mode = 'rb' if byte else 'r'
    return json.load(open(path, mode))


def json_dump(obj: Any, path: str, byte: bool=False) -> None:
    '''
        json.dump() that saves the open() wrapper 
    '''
    mode = 'wb' if byte else 'w'
    json.dump(obj, open(path, mode))
