import hashlib


def md5sum(path: str) -> str:
    with open(path, 'rb') as f:
        content = f.read()
        return hashlib.md5(content).hexdigest()
