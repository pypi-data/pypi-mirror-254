import os


def res(*av: str) -> str:
    return os.path.join(os.path.dirname(__file__), "resources", *av)
