import os
from dektools.shell import shell_wrapper
from dektools.file import normal_path


class InstallerBase:
    def __init__(self, path):
        self.path = normal_path(path)

    def run(self):
        raise NotImplementedError

    @staticmethod
    def exe(path, target=None):
        target = target or '/usr/local/bin'
        shell_wrapper(
            f'install {path} '
            f'{target}/{os.path.splitext(os.path.basename(path))[0]}'
        )


class InstallerBash(InstallerBase):
    def run(self):
        self.exe(self.path)


all_installer = {}


def register_installer(name):
    def wrapper(cls):
        all_installer[name] = cls

    return wrapper
