import rich
import typer

from inferless_cli.utils.constants import DEFAULT_YAML_FILE_NAME
from .utils.services import (
    callback_with_auth_validation,
    min_version_required,
)
from .utils.helpers import (
    check_import_source,
    sentry_init,
    set_env_mode,
    version_callback,
)
from .prompts import (
    init,
    login,
    workspace,
    token,
    deploy,
    log,
    model,
    secret,
    volume,
    runtime,
)
from prompt_toolkit import prompt
import sys
from inferless_cli import __version__

sys.tracebacklimit = 0

sentry_init()


app = typer.Typer(
    name="Inferless CLI",
    add_completion=False,
    rich_markup_mode="markdown",
    no_args_is_help=True,
    pretty_exceptions_enable=True,
    help="""
    Inferless - Deploy Machine Learning Models in Minutes.

    See the website at https://inferless.com/ for documentation and more information
    about running code on Inferless.
    """,
    callback=sentry_init,
)


@app.callback()
def inferless(
    ctx: typer.Context,
    version: bool = typer.Option(None, "--version", "-v", callback=version_callback),
):
    """
    This function is currently empty because it is intended to be used as a callback for the `inferless` command.
    The `inferless` command is not yet implemented, but this function is included here as a placeholder for future development.
    """
    pass


@app.command("mode", help="Change mode", hidden=True)
def run_mode(
    mode: str = typer.Argument(
        ..., help="The mode to run the application in, either 'DEV' or 'PROD'."
    )
):
    """
    Runs the application in the specified mode.
    """
    mode = mode.upper()  # Ensure mode is uppercase
    if mode not in ["DEV", "PROD"]:
        rich.print("[red]Error: Mode must be 'DEV' or 'PROD'[/red]")
        raise typer.Exit(code=1)

    if mode == "DEV":
        set_env_mode(mode)
        rich.print("[green]Running in development mode[/green]")
        # Insert your development mode code here
    else:
        set_env_mode(mode)
        rich.print("[green]Running in production mode[/green]")
        # Insert your production mode code here


app.add_typer(
    token.app,
    name="token",
    help="Manage Inferless tokens",
    callback=min_version_required,
)
app.add_typer(
    workspace.app,
    name="workspace",
    help="Manage Inferless workspaces (can be used to switch between workspaces)",
    callback=callback_with_auth_validation,
)
app.add_typer(
    model.app,
    name="model",
    help="Manage Inferless models (list , delete , activate , deactivate , rebuild the models)",
    callback=callback_with_auth_validation,
)
app.add_typer(
    secret.app,
    name="secret",
    help="Manage Inferless secrets (list secrets)",
    callback=callback_with_auth_validation,
)

app.add_typer(
    volume.app,
    name="volume",
    help="Manage Inferless volumes (can be used to list volumes and create new volumes)",
    callback=callback_with_auth_validation,
)

app.add_typer(
    runtime.app,
    name="runtime",
    help="Manage Inferless runtimes (can be used to list runtimes and upload new runtimes)",
    callback=callback_with_auth_validation,
)


@app.command("log", help="Inferless models logs (view build logs or call logs)")
def log_def(
    model_id: str = typer.Argument(None, help="Model id or model import id"),
    import_logs: bool = typer.Option(False, "--import-logs", "-i", help="Import logs"),
    logs_type: str = typer.Option(
        "BUILD", "--type", "-t", help="Logs type [BUILD, CALL]]"
    ),
):
    callback_with_auth_validation()
    log.log_prompt(model_id, logs_type, import_logs)


@app.command("init", help="Initialize a new Inferless model")
def init_def():
    callback_with_auth_validation()
    init.init_prompt()


@app.command("deploy", help="Deploy a model to Inferless")
def deploy_def():
    callback_with_auth_validation()
    config_file_name = prompt(
        "Enter the name of your config file: ", default=DEFAULT_YAML_FILE_NAME
    )
    if check_import_source(config_file_name) == "GIT":
        deploy.deploy_git(config_file_name)
    elif check_import_source(config_file_name) == "LOCAL":
        deploy.deploy_local(config_file_name, False)
    else:
        rich.print(
            "[red] config file not found [/red] please run [blue] inferless init [/blue] "
        )
        raise typer.Exit(1)


@app.command("login", help="Login to Inferless")
def login_def():
    min_version_required()
    login.login_prompt()


if __name__ == "__main__":
    app()
