from dektools.typer import command_mixin
from ..core.repository import Repository
from . import app


def main():
    app()


@command_mixin(app)
def install(args, name, version='', path='', typed=''):
    Repository(typed, *args.split(' ')).install(name, version or 'latest', path)


@app.command()
def sync(registry, username, password):
    repo_default = Repository('default')
    repo_coding = Repository('coding', registry, username, password)
    print(f"packages: {list(repo_default.packages)}", flush=True)
    for name, package in repo_default.packages.items():
        versions = package.versions[:3]
        print(f"versions({name}): {versions}")
        for version in versions:
            package_coding = repo_coding.packages[name]
            if package_coding.exist(version):
                print(f"skip {name}-{version} as exist", flush=True)
                continue
            path = package.pull(version)
            print(f"pulled {name}-{version}: {path}", flush=True)
            repo_coding.packages[name].push(path, version)
            print(f"pushed {name}-{version}", flush=True)
