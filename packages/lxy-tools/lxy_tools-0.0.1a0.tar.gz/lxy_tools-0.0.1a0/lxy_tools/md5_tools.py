import hashlib


def md5sum(path: str) -> str:
    '''
        MD5 sum of the content of a file
    '''
    with open(path, 'rb') as f:
        content = f.read()
        return hashlib.md5(content).hexdigest()
