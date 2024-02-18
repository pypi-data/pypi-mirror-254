from pathlib import Path
from dektools.file import write_file
from dektools.shell import shell_wrapper

path_shell = Path(__file__).resolve().parent.parent / 'resources/shell'


def shell_clone(path):
    write_file(path, c=path_shell)


def shell_run(name):
    shell_wrapper(f"bash {path_shell}/{name}.sh")
