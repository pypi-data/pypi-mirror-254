from . import app
from ..entries.base import all_entries


def main():
    app()


@app.command()
def install(name, path=''):
    all_entries[name](path).install()


@app.command()
def url(name, version):
    all_entries[name]().url_version(version)
