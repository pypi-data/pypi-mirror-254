import os
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import typer
from prompt_toolkit import prompt
import rich
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from inferless_cli.utils.constants import DEFAULT_YAML_FILE_NAME
from inferless_cli.utils.helpers import (
    key_bindings,
    create_yaml,
    decrypt_tokens,
    get_region_types,
    is_inferless_yaml_present,
    yaml,
)

from prompt_toolkit.validation import Validator
from inferless_cli.utils.services import (
    delete_volume_files_url,
    create_presigned_download_url,
    create_presigned_upload_url,
    get_file_download,
    get_volume_info,
    get_volume_info_with_id,
    get_volumes_list,
    create_volume,
    get_workspaces_list,
    sync_s3_to_nfs,
    sync_s3_to_s3,
    get_volume_files,
)
from inferless_cli.utils.validators import validate_region_types

app = typer.Typer(
    no_args_is_help=True,
)

processing = "processing..."
desc = "[progress.description]{task.description}"
no_volumes = "[red]No volumes found in your account[/red]"


@app.command(
    "list",
    help="List all existing volumes",
)
def list():
    _, _, _, workspace_id, _ = decrypt_tokens()

    with Progress(
        SpinnerColumn(),
        TextColumn(desc),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description=processing, total=None)

        volumes = get_volumes_list(workspace_id=workspace_id)

        progress.remove_task(task_id)

    if len(volumes) == 0:
        rich.print(no_volumes)
        raise typer.Exit(1)

    rich.print("\n[bold][underline]Volumes List[/underline][/bold]\n")
    for volume in volumes:
        volume_name = volume["name"]
        volume_id = volume["id"]
        path = volume["path"]
        region = volume["region"]
        rich.print(f"Volume: [bold]{volume_name}[/bold]")
        rich.print(f"ID: [bold]{volume_id}[/bold]")
        rich.print(f"Mount Path: [bold][purple]{path}[/purple][/bold]")
        rich.print(f"Region: [bold]{region}[/bold]")
        rich.print(
            f"Infer Path: [bold][purple]infer://volumes/{region}/{volume_name}[/purple][/bold]\n"
        )

    # console = Console()
    # console.print(table)
    # console.print("\n")


@app.command(
    "create",
    help="Create a new volume",
)
def create(
    name: str = typer.Option(
        None, "--name", "-n", help="Assign a name to the new volume."
    ),
):
    workspaces = get_workspaces_list()
    _, _, _, workspace_id, workspace_name = decrypt_tokens()
    if name is None:
        name = prompt(
            "Enter the name for volume: ",
        )
    is_aws_enabled = False
    for workspace in workspaces:
        if workspace["id"] == workspace_id:
            is_aws_enabled = workspace["is_aws_cluster_enabled"]
            break

    region = None
    if is_aws_enabled:
        region = prompt(
            "Select Region (AWS, AZURE, SERVERLESS_AWS) : ",
            completer=get_region_types(),
            complete_while_typing=True,
            key_bindings=key_bindings,
            validator=Validator.from_callable(validate_region_types),
            validate_while_typing=False,
        )
    else:
        region = "AZURE"
    res = None
    with Progress(
        SpinnerColumn(),
        TextColumn(desc),
        transient=True,
    ) as progress:
        task_id = progress.add_task(
            description=f"Creating model in [blue]{workspace_name}[/blue] workspace",
            total=None,
        )
        res = create_volume(workspace_id=workspace_id, name=name, region=region)
        progress.remove_task(task_id)

    if "id" in res and "name" in res:
        rich.print(f"[green]Volume {res['name']} created successfully[/green]")
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
                    config["configuration"]["custom_volume_id"] = res["id"]
                    config["configuration"]["custom_volume_name"] = res["name"]
                    create_yaml(config, DEFAULT_YAML_FILE_NAME)
                    rich.print(
                        f"[green]{DEFAULT_YAML_FILE_NAME} file updated successfully[/green]"
                    )


@app.command(
    "ls",
    help="List files and directories within a volume",
)
def list_files(
    id: str = typer.Option(
        None, "--id", "-i", help=" Specify the ID of the volume to list."
    ),
    path: str = typer.Option(
        None,
        "--path",
        "-p",
        help="Define a specific directory path within the volume. Defaults to the root directory if not specified.",
    ),
    directory_only: bool = typer.Option(
        False, "--directory", "-d", help="List only directories."
    ),
    files_only: bool = typer.Option(False, "--files", "-f", help="List only files."),
    recursive: bool = typer.Option(
        False, "--recursive", "-r", help="Recursively list contents of directories."
    ),
):
    _, _, _, workspace_id, _ = decrypt_tokens()
    if id is None:
        rich.print(
            "\n[red]Error: The --id option is required. Use `[blue]inferless volume list[/blue]` to find the volume id.[/red]\n"
        )
        raise typer.Exit(1)

    volume_data = find_volume_by_id(workspace_id, id)
    if volume_data is None:
        rich.print(f"[red]Error: No volume found with id {id}.[/red]")
        raise typer.Exit(1)

    volume_name = volume_data["name"]

    def list_directory(path, table):
        payload = {
            "volume_name": volume_name,
            "workspace_id": workspace_id,
            "volume_id": volume_data["id"],
        }

        if path != "":
            payload["file_path"] = path

        response = {}
        with Progress(
            SpinnerColumn(),
            TextColumn(desc),
            transient=True,
        ) as progress:
            task_id = progress.add_task("fetching files and directories")
            response = get_volume_files(payload)

        progress.remove_task(task_id)
        if not response["details"]:
            table.add_row(f"[yellow]No files or directories found at '{path}'[/yellow]")

        for item in response["details"]:
            if directory_only and item["type"] != "directory":
                continue
            if files_only and item["type"] != "file":
                continue

            path_new = path + "/" if path else ""

            table.add_row(
                f"[blue]{path_new}{item['name']}[/blue]",
                item["type"],
                str(item["file_size"]),
                item["created_at"],
            )
            if recursive and item["type"] == "directory":
                list_directory(f"{path_new}{item['name']}", table)

    table = Table(show_header=False, box=None)
    list_directory(path or "", table)
    rich.print(
        f"\n [green][bold]Volume: {volume_name}[/bold][/green] (Path: {path or '/'}) \n"
    )
    rich.print(table)
    rich.print("\n")
    if not recursive:
        rich.print(
            f"You can run `[blue]inferless volume ls -i {id} -p DIR_NAME[/blue]` for viewing files inside dir\n"
        )
        rich.print(
            "[green]Tip: Use the --recursive (-r) flag to list contents of directories recursively.[/green]\n\n"
        )


@app.command(
    "select", help="Select a volume for updates in the Inferless configuration."
)
def select(
    path: str = typer.Option(
        None,
        "--path",
        "-p",
        help="Path to the Inferless configuration file (typically inferless.yaml)",
    ),
    id: str = typer.Option(None, "--id", "-i", help="The ID of the volume to select."),
):
    _, _, _, workspace_id, _ = decrypt_tokens()
    if id is None:
        rich.print(
            "\n[red]--id is required. Please use `[blue]inferless volume list[/blue]` to get the id[/red]\n"
        )
        raise typer.Exit(1)

    if path is None:
        path = prompt(
            "Enter path of inferless config file : ",
            default="%s" % DEFAULT_YAML_FILE_NAME,
        )

    volume = find_volume_by_id(workspace_id, id)

    if not volume:
        rich.print(
            "\n[red]Volume with id [blue]%s[/blue] not found in your workspace[/red]\n"
            % id
        )
        raise typer.Exit(1)

    rich.print("Updating yaml file")
    with open(path, "r") as yaml_file:
        config = yaml.load(yaml_file)
        config["configuration"]["custom_volume_name"] = volume["name"]
        config["configuration"]["custom_volume_id"] = volume["id"]
        create_yaml(config, DEFAULT_YAML_FILE_NAME)
        rich.print(f"[green]{DEFAULT_YAML_FILE_NAME} file updated successfully[/green]")


@app.command("cp", help="Add a file or directory to a volume.")
def copy(
    source: str = typer.Option(
        None,
        "--source",
        "-s",
        help="Specify the source path (either a local directory/file path or an Inferless path)",
    ),
    destination: str = typer.Option(
        None,
        "--destination",
        "-d",
        help="Specify the destination path (either a local directory/file path or an Inferless path)",
    ),
):
    _, _, _, workspace_id, _ = decrypt_tokens()

    if not source:
        rich.print("\n[red]--source is a required param")
        raise typer.Exit(1)
    if not destination:
        rich.print("\n[red]--destination is a required param")
        raise typer.Exit(1)

    if source and not source.startswith("infer://"):
        source = make_absolute(source)
    elif destination and not destination.startswith("infer://"):
        destination = make_absolute(destination)

    volume_name = ""
    cp_type = None
    if source.startswith("infer://"):
        volume_name, volume_region = extract_volume_info(source)
        cp_type = "DOWNLOAD"
    elif destination.startswith("infer://"):
        volume_name, volume_region = extract_volume_info(destination)
        cp_type = "UPLOAD"
    else:
        rich.print("\n[red]--source or --destination should start with infer://")
        raise typer.Exit(1)

    volume_data = find_volume_by_name(workspace_id, volume_name, volume_region)
    if volume_data is None:
        rich.print(f"[red]Error: No volume found with {volume_name}.[/red]")
        raise typer.Exit(1)

    try:
        if cp_type == "UPLOAD":
            with concurrent.futures.ThreadPoolExecutor() as executor:
                s3_path = destination.split("infer://")[1]
                vol_id = volume_data["id"]
                vol_region = volume_data["region"]

                s3_path = s3_path.replace(
                    f"volumes/{vol_region}/",
                    f"volumes_temp/{vol_region}/{workspace_id}/{vol_id}/",
                )

                volume_data["volume_id"] = volume_data["id"]
                futures = []
                if os.path.isfile(source):
                    futures.append(
                        executor.submit(
                            process_file,
                            source,
                            s3_path,
                            source,
                        )
                    )

                elif os.path.isdir(source):
                    futures += process_directory(
                        executor,
                        source,
                        s3_path,
                        source,
                    )

                results = [future.result() for future in futures]
                if all(results):
                    s3_path_original = s3_path.replace(
                        f"volumes_temp/{vol_region}/", f"volumes/{vol_region}/"
                    )
                    payload = {"source": s3_path, "destination": s3_path_original}
                    res = sync_s3_to_s3(payload)

                    base_s3_path = os.path.join(
                        "volumes",
                        volume_data["region"] if volume_data["region"] else "AZURE",
                        workspace_id,
                        volume_data["id"],
                        volume_data["name"],
                    )
                    vol_id = volume_data["id"]
                    sync_s3_to_nfs({"s3_path": base_s3_path, "volume_id": vol_id})
                    rich.print("\n[green]Upload successful[/green]\n\n")
        if cp_type == "DOWNLOAD":
            with Progress(
                SpinnerColumn(),
                TextColumn(desc),
                transient=True,
            ) as progress:
                task_id = progress.add_task(description="Downloading..", total=None)
                s3_path = source.split("infer://")[1]
                vol_id = volume_data["id"]
                region = volume_data["region"]
                s3_path = s3_path.replace(
                    f"volumes/{region}/", f"volumes/{region}/{workspace_id}/{vol_id}/"
                )
                payload = {
                    "url_for": "VOLUME_FOLDER_DOWNLOAD",
                    "file_name": f"{s3_path}",
                }
                res = create_presigned_download_url(payload)
                download_files_in_parallel(res, destination)
                progress.remove_task(task_id)
            rich.print(
                f"[green]downloaded successfully and saved at '{destination}'[/green]"
            )

    except Exception as e:
        rich.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@app.command(
    "rm", help="Specify the Inferless path to the file or directory you want to delete."
)
def delete(
    path: str = typer.Option(
        None, "--path", "-p", help="Infer Path to the file/dir your want to delete"
    ),
):
    _, _, _, workspace_id, _ = decrypt_tokens()
    volume_name, volume_region = extract_volume_info(path)
    if id is None:
        rich.print(
            "\n[red]--id is required. Please use `[blue]inferless volume list[/blue]` to get the id[/red]\n"
        )
        raise typer.Exit(1)

    volume_data = find_volume_by_name(workspace_id, volume_name, volume_region)
    if volume_data is None:
        rich.print(f"[red]Error: No volume found with name {volume_name}.[/red]")
        raise typer.Exit(1)

    with Progress(
        SpinnerColumn(),
        TextColumn(desc),
        transient=True,
    ) as progress:
        task_id = progress.add_task(description="deleting...", total=None)
        base_s3_path = os.path.join(
            "volumes",
            volume_data["region"] if "region" in volume_data else "AZURE",
            workspace_id,
            volume_data["id"],
            volume_data["name"],
        )
        region = volume_data["region"] if "region" in volume_data else "AZURE"
        vol_id = volume_data["id"]
        s3_path = path.split("infer://")[1]
        s3_path = s3_path.replace(
            f"volumes/{region}/", f"volumes/{region}/{workspace_id}/{vol_id}/"
        )

        payload = {"s3_path": s3_path, "volume_id": vol_id}
        res = delete_volume_files_url(payload)

        if res == "Deleted Successfully":
            try:
                sync_s3_to_nfs({"s3_path": base_s3_path, "volume_id": vol_id})
            except Exception as e:
                rich.print(f"[red]Error in syncing: {e}[/red]")

            rich.print("[green]File successfully deleted.[/green]")
        else:
            rich.print("[red]Failed to delete file.[/red]")

        progress.remove_task(task_id)


def find_volume_by_name(workspace_id, volume_name, volume_region):
    volume = get_volume_info(workspace_id, volume_name, volume_region)
    return volume


def find_volume_by_id(workspace_id, volume_id):
    volume = get_volume_info_with_id(workspace_id, volume_id)

    return volume


def process_file(path: str, s3_path, root_path):
    temp = path.split(root_path)[-1]
    save_path = os.path.join(s3_path, temp.lstrip("/"))
    if save_path.startswith("/"):
        save_path = save_path[1:]

    payload = {
        "url_for": "VOLUME_FILE_UPLOAD",
        "file_name": save_path,
    }
    res = create_presigned_upload_url(payload, path)
    if "status" in res and res["status"] == "success":
        return True


def process_directory(executor, dir_path: str, s3_path, root_path):
    futures = []
    for root, dirs, files in os.walk(dir_path):
        # Process each directory within the root directory
        # for dir in dirs:
        #     dir_path = os.path.join(root, dir)
        #     # Generate presigned URL for the directory
        #     futures += process_directory(executor, dir_path, s3_path, root_path)

        # Process each file within the root directory
        for file in files:
            file_path = os.path.join(root, file)
            future = executor.submit(process_file, file_path, s3_path, root_path)
            futures.append(future)

    return futures


def extract_volume_info(input_string):
    # Splitting the URL by '/'
    parts = input_string.split("/")

    # Extracting workspace_id, volume_id, and volume_name
    # The indices are based on the structure of your URL
    volume_region = parts[3] if len(parts) > 3 else None
    volume_name = parts[4] if len(parts) > 4 else None

    return volume_name, volume_region


def make_request(url, destination):
    response = get_file_download(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        with open(destination, "wb") as file:
            file.write(response.content)
    else:
        rich.print(f"Failed to download {url}")


def download_files_in_parallel(file_dict, dest):
    # Using ThreadPoolExecutor to download files in parallel
    with ThreadPoolExecutor() as executor:
        # Creating a list of futures
        futures = []
        for local_path, url in file_dict.items():
            destination = os.path.join(dest, local_path)
            rich.print(f"Downloading {local_path} to {destination}")
            # Submitting the download task
            futures.append(executor.submit(make_request, url, destination))

        # Waiting for all futures to complete
        for future in futures:
            future.result()


def make_absolute(path):
    # Check if the path is either '.' (current directory) or a relative path
    if path == "." or not os.path.isabs(path):
        # Use os.path.abspath to convert to an absolute path
        return os.path.abspath(path)
    else:
        # If the path is already absolute, return it as is
        return path
