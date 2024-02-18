from prompt_toolkit.validation import Validator
import typer
from prompt_toolkit import prompt
import rich
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.console import Console
from inferless_cli.utils.constants import (
    DEFAULT_RUNTIME_FILE_NAME,
    DEFAULT_YAML_FILE_NAME,
)
from inferless_cli.utils.helpers import (
    create_yaml,
    decrypt_tokens,
    yaml,
    is_inferless_yaml_present,
)
import os

from inferless_cli.utils.services import (
    create_presigned_url,
    get_templates_list,
)
import uuid

app = typer.Typer(
    no_args_is_help=True,
)

processing = "processing..."
desc = "[progress.description]{task.description}"
no_runtimes = "[red]No runtimes found in your account[/red]"


@app.command(
    "list",
    help="List all runtimes.",
)
def list():
    _, _, _, workspace_id, _ = decrypt_tokens()
    with Progress(
        SpinnerColumn(),
        TextColumn(desc),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description=processing, total=None)

        runtimes = get_templates_list(workspace_id)

        progress.remove_task(task_id)

    if len(runtimes) == 0:
        rich.print(no_runtimes)
        raise typer.Exit(1)

    table = Table(
        title="Runtime List",
        box=rich.box.ROUNDED,
        title_style="bold Black underline on white",
    )
    table.add_column("ID", style="yellow")
    table.add_column(
        "Name",
    )
    table.add_column("Status")

    for runtime in runtimes:
        table.add_row(
            runtime["id"],
            runtime["name"],
            runtime["status"],
        )

    console = Console()
    console.print(table)
    console.print("\n")


@app.command("upload", help="Upload a runtime.")
def upload(
    path: str = typer.Option(None, "--path", "-p", help="Path to the runtime"),
    name: str = typer.Option(None, "--name", "-n", help="Name of the runtime"),
):
    _, _, _, workspace_id, _ = decrypt_tokens()
    if path is None:
        path = prompt(
            "Enter path of yaml file : ",
            default="%s" % DEFAULT_RUNTIME_FILE_NAME,
        )

    if name is None:
        name = prompt(
            "Enter the name for runtime: ",
        )

    uid = uuid.uuid4()
    file_name = os.path.basename(path)
    payload = {
        "url_for": "YAML_FILE_UPLOAD",
        "file_name": f'{uid}/{file_name.replace(" ", "")}',
    }
    res = None
    with Progress(
        SpinnerColumn(),
        TextColumn(desc),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description="Uploading runtime config", total=None)
        res = create_presigned_url(
            payload,
            uid,
            name,
            file_name.replace(" ", ""),
            path,
            workspace_id,
        )
        progress.remove_task(task_id)
    if "id" in res and "name" in res:
        rich.print(f"[green]Runtime {res['name']} uploaded successfully[/green]")
        is_yaml_present = is_inferless_yaml_present(DEFAULT_YAML_FILE_NAME)

        if is_yaml_present:
            is_update = typer.confirm(
                f"Found {DEFAULT_YAML_FILE_NAME} file. Do you want to update it? ",
                default=True,
            )
            if is_update == True:
                rich.print("Updating yaml file")
                with open(DEFAULT_YAML_FILE_NAME, "r") as yaml_file:
                    config = yaml.load(yaml_file)
                    config["configuration"]["custom_runtime_id"] = res["id"]
                    create_yaml(config, DEFAULT_YAML_FILE_NAME)
                    rich.print(
                        f"[green]{DEFAULT_YAML_FILE_NAME} file updated successfully[/green]"
                    )


@app.command("select", help="use to update the runtime in inferless config file")
def select(
    path: str = typer.Option(
        None, "--path", "-p", help="Path to the inferless config file (inferless.yaml)"
    ),
    id: str = typer.Option(None, "--id", "-i", help="runtime id"),
):
    if id is None:
        rich.print(
            "\n[red]--id is required. Please use `[blue]inferless runtime list[/blue]` to get the id[/red]\n"
        )
        raise typer.Exit(1)

    if path is None:
        path = prompt(
            "Enter path of inferless config file : ",
            default="%s" % DEFAULT_YAML_FILE_NAME,
        )

    rich.print("Updating yaml file")
    with open(path, "r") as yaml_file:
        config = yaml.load(yaml_file)
        config["configuration"]["custom_runtime_id"] = id
        create_yaml(config, DEFAULT_YAML_FILE_NAME)
        rich.print(f"[green]{DEFAULT_YAML_FILE_NAME} file updated successfully[/green]")
