from importlib.metadata import version as get_version
from pathlib import Path

import typer
from slugify import slugify as awslugify
from turbofan import command, project

package_name = "groundsupport"
app = typer.Typer(add_completion=False, help=project.summary(package_name))


# -------------------------------------------------------------------------------------------------
@app.command()
def slugify(
    text: str = typer.Argument(..., help="The string to slugify, between commas."),
):
    """
    Slugifies a string to lower case by default.
    """
    print(f"\n\t{awslugify(text, to_lower=True)}")


@app.command()
def version():
    """
    Shows the current version.
    """
    typer.echo(get_version(package_name))


projects_app = typer.Typer()
app.add_typer(projects_app, name="projects", help="Project management commands.")


@projects_app.command(
    help="Cleans all projects found in the specified path, according to the project Makefile."
)
def clean(path: str = typer.Argument(".", help="The path to the projects.")):
    """
    Run clean executes 'make clean' in all subdirectories from the execution
    of the command.
    """

    for path in Path(path).glob("*/Makefile"):
        typer.echo(f"Running make clean in {path.parent}")
        command.Command(["make", "-C", path.parent, "clean"]).run()


if __name__ == "__main__":
    app()
