import logging
import dateutil
import typer
import rich
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.console import Console

from inferless_cli.utils.services import (
    get_user_secrets,
)


app = typer.Typer(
    no_args_is_help=True,
)

processing = "processing..."
desc = "[progress.description]{task.description}"
no_secrets = "[red]No secrets found in your account[/red]"


@app.command(
    "list",
    help="List all secrets.",
)
def list():
    with Progress(
        SpinnerColumn(),
        TextColumn(desc),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description=processing, total=None)

        secrets = get_user_secrets()

        progress.remove_task(task_id)

    if len(secrets) == 0:
        rich.print(no_secrets)
        raise typer.Exit(1)

    table = Table(
        title="Secrets List",
        box=rich.box.ROUNDED,
        title_style="bold Black underline on white",
    )
    table.add_column("ID", style="yellow")
    table.add_column(
        "Name",
    )
    table.add_column("Created At")
    table.add_column("Last used on")

    for secret in secrets:
        created_at = "-"
        updated_at = "-"
        try:
            created_at = dateutil.parser.isoparse(secret["created_at"]).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        except Exception as e:
            logging.error(e)
        try:
            updated_at = dateutil.parser.isoparse(
                secret["last_used_in_model_import"]
            ).strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            logging.error(e)

        table.add_row(
            secret["id"],
            secret["name"],
            created_at,
            updated_at,
        )

    console = Console()
    console.print(table)
    console.print("\n")
