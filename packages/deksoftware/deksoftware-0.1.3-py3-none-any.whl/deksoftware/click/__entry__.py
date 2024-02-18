from . import app
from ..entries.base import all_entries
from .shell import app as shell_app

app.add_typer(shell_app, name='shell')


def main():
    app()


@app.command()
def install(name, path=''):
    all_entries[name](path).install()


@app.command()
def url(name, version):
    all_entries[name]().url_version(version)
