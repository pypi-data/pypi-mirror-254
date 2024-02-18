import os
import functools
from pathlib import Path


class EntryBase:
    homepage = None
    release = None
    name_src = None
    name_res = None

    def __init__(self, path=None):
        self.path_nest = Path(path).resolve() if path else None

    @property
    @functools.lru_cache(None)
    def path_res(self):
        return Path(__file__).resolve().parent.parent.parent / 'resources' / self.name_res

    @property
    @functools.lru_cache(None)
    def paths_src(self):
        return list(self.find_src())

    def url_version(self, version):
        return self.release.format(version=version)

    def find_src(self):
        if os.path.isfile(self.path_nest):
            yield self.path_nest
        elif self.name_src and os.path.isdir(self.path_nest):
            for file in os.listdir(self.path_nest):
                if self.name_src in file:
                    yield os.path.join(self.path_nest, file)

    def install(self):
        raise NotImplementedError


all_entries = {}


def register(name):
    def wrapper(cls):
        all_entries[name] = cls

    return wrapper
