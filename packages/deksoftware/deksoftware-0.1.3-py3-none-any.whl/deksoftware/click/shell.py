import typer
from ..shell import shell_run, shell_clone

app = typer.Typer(add_completion=False)


@app.command()
def clone(path):
    shell_clone(path)


@app.command()
def run(name):
    shell_run(name)
