import json
import logging
import os
import webbrowser
import zipfile
import rich
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import typer
from urllib.parse import urlparse
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
import keyring
import toml
import jwt
from datetime import datetime, timezone
from rich.rule import Rule
import importlib.util
from inferless_cli import __version__
from ruamel.yaml import YAML
from sentry_sdk import capture_exception
import signal

from .constants import (
    DEFAULT_YAML_FILE_NAME,
    DEPLOYMENT_TYPE,
    FRAMEWORKS,
    GLITCHTIP_DSN,
    MACHINE_TYPE_SERVERS,
    MACHINE_TYPES_SERVERLESS,
    REGION_TYPES,
    UPLOAD_METHODS,
    HF_TASK_TYPE,
    HUGGINGFACE_TYPE,
    MACHINE_TYPES,
    DEFAULT_MACHINE_VALUES,
    DOCS_URL,
    APP_PY,
    MODEL_ONNX,
)
import subprocess

yaml = YAML(typ="rt")

key_bindings = KeyBindings()


def get_default_machine_values(gpu_type, is_dedicated):
    if is_dedicated not in DEFAULT_MACHINE_VALUES:
        return None
    if gpu_type not in DEFAULT_MACHINE_VALUES[is_dedicated]:
        return None
    return DEFAULT_MACHINE_VALUES[is_dedicated][gpu_type]


def save_cli_tokens(key, secret):
    try:
        keyring.set_password("Inferless", "key", key)
        keyring.set_password("Inferless", "secret", secret)
    except Exception as e:
        log_exception(e)
        rich.print(f"An error occurred while saving the tokens: {e}")


def set_env_mode(mode):
    try:
        keyring.set_password("Inferless", "mode", mode)
    except Exception as e:
        log_exception(e)
        rich.print(f"An error occurred while saving the env: {e}")


def save_tokens(token, refresh_token, user_id, workspace_id, workspace_name):
    try:
        keyring.set_password("Inferless", "token", token)
        keyring.set_password("Inferless", "refresh_token", refresh_token)
        keyring.set_password("Inferless", "user_id", user_id)
        keyring.set_password("Inferless", "workspace_id", workspace_id)
        keyring.set_password("Inferless", "workspace_name", workspace_name)
    except Exception as e:
        log_exception(e)
        rich.print(f"An error occurred while saving the tokens: {e}")


def create_yaml(config, file_name=DEFAULT_YAML_FILE_NAME):
    try:
        with open(file_name, "w") as yaml_file:
            yaml.dump(
                config,
                yaml_file,
            )
    except Exception as e:
        log_exception(e)
        rich.print("Failed to create YAML file: {}".format(e))


@key_bindings.add("c-space")
def _(event):
    """
    Start auto completion. If the menu is showing already, select the next
    completion.
    """
    b = event.app.current_buffer
    if b.complete_state:
        b.complete_next()
    else:
        b.start_completion(select_first=False)


def get_frameworks():
    return WordCompleter(
        FRAMEWORKS,
        ignore_case=True,
    )


def get_deployment_types():
    return WordCompleter(
        DEPLOYMENT_TYPE,
        ignore_case=True,
    )


def get_task_types():
    return WordCompleter(
        [item["value"] for item in HF_TASK_TYPE],
        ignore_case=True,
    )


def get_volumes(volumes):
    return WordCompleter(
        [item["name"] for item in volumes],
        ignore_case=True,
    )


def get_templates(templates):
    return WordCompleter(
        [item["name"] for item in templates],
        ignore_case=True,
    )


def get_models(models):
    return WordCompleter(
        [item["name"] for item in models],
        ignore_case=True,
    )


def get_workspaces(workspaces):
    return WordCompleter(
        [item["name"] for item in workspaces],
        ignore_case=True,
    )


def get_machine_types():
    return WordCompleter(
        MACHINE_TYPES,
        ignore_case=True,
    )


def get_machine_types_serverless():
    return WordCompleter(
        MACHINE_TYPES_SERVERLESS,
        ignore_case=True,
    )


def get_region_types():
    return WordCompleter(
        REGION_TYPES,
        ignore_case=True,
    )


def get_machine_types_servers():
    return WordCompleter(
        MACHINE_TYPE_SERVERS,
        ignore_case=True,
    )


def get_huggingface_types():
    return WordCompleter(
        [item["value"] for item in HUGGINGFACE_TYPE],
        ignore_case=True,
    )


def get_upload_methods():
    return WordCompleter(
        UPLOAD_METHODS,
        ignore_case=True,
    )


def print_options(options_name, options):
    console = rich.console.Console()
    console.print("\n")
    console.print(f"{options_name}", style="bold")

    for method in options:
        console.print(f"  • {method}", style="green")
    console.print("\n")


def version_callback(value: bool):
    if value:
        typer.echo(f"inferless-cli version: {__version__}")
        raise typer.Exit()


# Function to decrypt tokens
def decrypt_tokens():
    try:
        token = keyring.get_password("Inferless", "token")
        refresh_token = keyring.get_password("Inferless", "refresh_token")
        user_id = keyring.get_password("Inferless", "user_id")
        workspace_id = keyring.get_password("Inferless", "workspace_id")
        workspace_name = keyring.get_password("Inferless", "workspace_name")
        return token, refresh_token, user_id, workspace_id, workspace_name
    except Exception as e:
        log_exception(e)
        return None, None, None, None, None


def is_inferless_yaml_present(file_path=DEFAULT_YAML_FILE_NAME):
    file_name = file_path
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_name)

    return os.path.isfile(file_path)


def decrypt_cli_key():
    try:
        key = keyring.get_password("Inferless", "key")
        refresh_token = keyring.get_password("Inferless", "secret")
        return key, refresh_token
    except Exception as e:
        log_exception(e)
        return None, None


def validate_jwt(jwt_token):
    try:
        # Decode the JWT token without verifying it (no secret key)
        payload = jwt.decode(
            jwt_token, options={"verify_signature": False}, algorithms="HS256"
        )
        # Check if the 'exp' (expiration) claim exists and is in the future
        if "exp" in payload:
            exp_timestamp = payload["exp"]
            if isinstance(exp_timestamp, int):
                current_timestamp = datetime.now(timezone.utc).timestamp()
                if exp_timestamp >= current_timestamp:
                    # Token is not expired
                    return True
                else:
                    # Token has expired
                    return False
            else:
                # 'exp' claim is not an integer
                return False
        else:
            # 'exp' claim is missing
            return False

    except jwt.ExpiredSignatureError as e:
        log_exception(e)
        # Token has expired
        return False
    except jwt.InvalidTokenError as e:
        log_exception(e)
        # Token is invalid or tampered with
        return False


def generate_input_and_output_files(
    input_data,
    output_data,
    input_file_name="input.json",
    output_file_name="output.json",
):
    """
    Generate input and output JSON files.

    Args:
        input_data (dict): The data to be saved in the input JSON file.
        output_data (dict): The data to be saved in the output JSON file.
        input_file_name (str): The name of the input JSON file. Default is 'input.json'.
        output_file_name (str): The name of the output JSON file. Default is 'output.json'.

    Returns:
        None
    """
    # Save the input data to input.json
    try:
        with open(input_file_name, "w") as input_file:
            json.dump(input_data, input_file, indent=4)
    except Exception as e:
        log_exception(e)
        rich.print("An error occurred while saving the input data.")
        raise typer.Exit()

    # Save the output data to output.json
    try:
        with open(output_file_name, "w") as output_file:
            json.dump(output_data, output_file, indent=4)
    except Exception as e:
        log_exception(e)
        rich.print("An error occurred while saving the output data.")
        raise typer.Exit()


def get_by_keys(data, value, key1, key2):
    if data is None:
        raise ValueError("data is None")
    if value is None:
        raise ValueError("value is None")
    if key1 is None:
        raise ValueError("key1 is None")
    if key2 is None:
        raise ValueError("key2 is None")
    for item in data:
        if item.get(key1) == value:
            return item.get(key2)
    return None


def check_path():
    """Checks whether the `inferless` executable is on the path and usable."""

    try:
        subprocess.run(["inferless", "--help"], capture_output=True)
        return
    except FileNotFoundError as e:
        log_exception(e)
        text = (
            "[red]The `[white]modal[/white]` command was not found on your path!\n"
            "You may need to add it to your path or use `[white]python -m modal[/white]` as a workaround.[/red]\n"
        )
    except PermissionError as e:
        log_exception(e)
        text = (
            "[red]The `[white]inferless[/white]` command is not executable!\n"
            "You may need to give it permissions or use `[white]python -m inferless[/white]` as a workaround.[/red]\n"
        )
    text += "See more information here:\n\n" f"[link={DOCS_URL}]{DOCS_URL}[/link]\n"

    rich.print(text)
    rich.print(Rule(style="white"))


def open_url(url: str) -> bool:
    try:
        browser = webbrowser.get()
        if isinstance(browser, webbrowser.GenericBrowser):
            return False
        if not hasattr(browser, "open_new_tab"):
            return False
        return browser.open_new_tab(url)
    except webbrowser.Error as e:
        log_exception(e)
        return False


def check_file_structure():
    if os.path.exists(APP_PY):
        # Import app.py as a module
        spec = importlib.util.spec_from_file_location("app", APP_PY)
        app_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app_module)

        # Check if InferlessPythonModel class is present
        if hasattr(app_module, "InferlessPythonModel"):
            # Check if the class has the required methods
            model_class = app_module.InferlessPythonModel
            required_methods = ["initialize", "infer", "finalize"]
            missing_methods = [
                method
                for method in required_methods
                if not hasattr(model_class, method)
            ]

            if not missing_methods:
                return True, None
            else:
                return (
                    False,
                    f"app.py is present, but InferlessPythonModel is missing the following methods: {', '.join(missing_methods)}",
                )

        else:
            return (
                False,
                "app.py is present, but InferlessPythonModel class is missing.",
            )
    elif os.path.exists(MODEL_ONNX):
        return True, None
    else:
        return False, "structure not found"


def check_import_source(file_name):
    if os.path.isfile(file_name):
        try:
            with open(file_name, "r") as yaml_file:
                inferless_config = yaml.load(yaml_file)
                import_source = inferless_config.get("import_source", "")
                return import_source
        except Exception as e:
            log_exception(e)
            rich.print("Failed to read YAML file: {}".format(e))

    return None


def read_yaml(file_name):
    if os.path.isfile(file_name):
        with open(file_name, "r") as yaml_file:
            try:
                inferless_config = yaml.load(yaml_file)
                return inferless_config
            except Exception as e:
                log_exception(e)
                rich.print("Failed to read YAML file: {}".format(e))
    return None


def read_json(file_name):
    try:
        with open(file_name, "r") as json_file:
            file_data = json.load(json_file)
            return file_data
    except Exception as e:
        log_exception(e)
        return None


def create_zip_file(zip_filename, directory_to_snapshot):
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory_to_snapshot):
            for file in files:
                zipf.write(
                    os.path.join(root, file),
                    os.path.relpath(
                        os.path.join(root, file),
                        directory_to_snapshot,
                    ),
                )


def find_requirements_file():
    current_dir = os.getcwd()

    requirements_path = os.path.join(current_dir, "requirements.txt")
    pyproject_path = os.path.join(current_dir, "pyproject.toml")

    if os.path.isfile(requirements_path):
        return requirements_path, "txt", "requirements.txt"
    elif os.path.isfile(pyproject_path):
        return pyproject_path, "toml", "pyproject.toml"
    else:
        return None, None, None


def read_requirements_txt(file_path):
    try:
        with open(file_path, "r") as file:
            return [
                line.strip()
                for line in file.readlines()
                if not line.strip().startswith("#")
            ]
    except:
        rich.print(f"[red]An error occurred while reading {file_path}[/red]")
        return []


def read_pyproject_toml(file_path):
    try:
        with open(file_path, "r") as file:
            pyproject_data = toml.load(file)
            dependencies = (
                pyproject_data.get("tool", {}).get("poetry", {}).get("dependencies", {})
            )
            return [
                f"{package}=={version}" for package, version in dependencies.items()
            ]
    except Exception as e:
        log_exception(e)
        rich.print(f"[red]An error occurred while reading {file_path}[/red]")
        return []


def log_exception(e):
    capture_exception(e)


def sentry_init():
    if GLITCHTIP_DSN:
        sentry_sdk.init(
            dsn=GLITCHTIP_DSN,
            auto_session_tracking=False,
            integrations=[
                LoggingIntegration(
                    level=logging.INFO,  # Capture info and above as breadcrumbs
                    event_level=logging.ERROR,  # Send errors as events
                ),
            ],
            traces_sample_rate=0.01,
            release=__version__,
            send_default_pii=True,
            environment="dev",
        )


def sync_folder_validator(path: str) -> (bool, str):
    """
    Validates the path for sync_folder command, checks the num files and size of the folder
    :param path: path of the folder to be synced
    :return: num_files, is_valid
    """
    timeout = 30
    # check if the path exists
    if not os.path.exists(path):
        return False, "Path does not exist"

    class TimeoutError(Exception):
        pass

    def timeout_handler(signum, frame):
        raise TimeoutError("Exceeded time limit")

    try:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout)

        file_count = 0
        total_size = 0
        for root, dirs, files in os.walk(path):
            file_count += len(files)
            if file_count > 1000:
                raise Exception("Too many files, max 1000 files allowed")
            for file in files:
                total_size += os.path.getsize(os.path.join(root, file))
                # max 100GB allowed
            if total_size > 100 * 1024 * 1024 * 1024:
                raise Exception("Too large folder, max 100GB allowed")
            if total_size == 0:
                raise Exception("Empty folder not allowed")
    except TimeoutError:
        return False, "Took too long to validate the folder"
    except Exception as e:
        return False, str(e)
    finally:
        signal.alarm(0)

    return True, ""


def is_file_present(file_name):
    """
    Check if 'input_schema.py' is present in the current working directory.

    Returns:
    bool: True if the file is found, False otherwise.
    """
    # Get the current working directory
    current_directory = os.getcwd()

    # Combine the directory and the file name
    file_path = os.path.join(current_directory, file_name)

    # Check if the file exists at the specified path
    return os.path.isfile(file_path)
