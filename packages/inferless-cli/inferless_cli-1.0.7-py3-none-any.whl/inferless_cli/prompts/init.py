import typer
from inferless_cli.utils.services import get_connected_accounts
from inferless_cli.utils.helpers import (
    create_yaml,
    get_machine_types_serverless,
    get_machine_types_servers,
    is_file_present,
    yaml,
    find_requirements_file,
    get_default_machine_values,
    get_deployment_types,
    get_frameworks,
    get_upload_methods,
    key_bindings,
    generate_input_and_output_files,
    get_machine_types,
    print_options,
    read_pyproject_toml,
    read_requirements_txt,
)
from inferless_cli.utils.services import (
    get_connected_accounts,
)
from inferless_cli.utils.validators import (
    has_github_provider,
    validate_deployment_type,
    validate_framework,
    validate_machine_types,
    validate_machine_types_server,
    validate_machine_types_serverless,
    validate_upload_method,
    validate_model_name,
    validate_url,
)
from inferless_cli.utils.constants import (
    DEFAULT_INFERLESS_RUNTIME_YAML_FILE,
    DEFAULT_INFERLESS_YAML_FILE,
    DEFAULT_RUNTIME_FILE_NAME,
    DEFAULT_YAML_FILE_NAME,
    DEPLOYMENT_TYPE,
    FRAMEWORKS,
    GITHUB,
    GIT,
    DEFAULT_INPUT_JSON,
    DEFAULT_OUTPUT_JSON,
    DEFAULT_INPUT_FILE_NAME,
    DEFAULT_OUTPUT_FILE_NAME,
    IO_DOCS_URL,
    MACHINE_TYPE_SERVERS,
    MACHINE_TYPE_SERVERS_DEF,
    MACHINE_TYPES,
    MACHINE_TYPES_SERVERLESS,
    RUNTIME_DOCS_URL,
    UPLOAD_METHODS,
)
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator
from rich.progress import Progress, SpinnerColumn, TextColumn
import rich

processing = "processing..."
desc = "[progress.description]{task.description}"


def init_prompt():
    """Prompt the user for configuration parameters."""
    rich.print("Welcome to the Inferless Model Initialization!")

    config_file_name = prompt(
        "Enter config file name: ",
        default="%s" % DEFAULT_YAML_FILE_NAME,
    )

    import_source = prompt(
        f"How do you want to upload the model ({', '.join(str(x) for x in UPLOAD_METHODS)}) ?  ",
        completer=get_upload_methods(),
        complete_while_typing=True,
        key_bindings=key_bindings,
        validator=Validator.from_callable(validate_upload_method),
        validate_while_typing=False,
    )

    import_framework_type = prompt(
        f"Select framework ({', '.join(str(x) for x in FRAMEWORKS)}): ",
        completer=get_frameworks(),
        complete_while_typing=True,
        key_bindings=key_bindings,
        validator=Validator.from_callable(validate_framework),
        validate_while_typing=False,
    )

    name = prompt(
        "Model name: ",
        validator=Validator.from_callable(validate_model_name),
    )

    config = yaml.load(DEFAULT_INFERLESS_YAML_FILE)

    config["source_framework_type"] = import_framework_type
    config["name"] = name

    #
    # Get connected accounts
    accounts = []
    if import_source == GIT:
        with Progress(
            SpinnerColumn(),
            TextColumn(desc),
            transient=True,
        ) as progress:
            task_id = progress.add_task(description=processing, total=None)
            accounts = get_connected_accounts(import_source)
            progress.remove_task(task_id)

        # exit if no connected accounts found
        if len(accounts) == 0:
            rich.print(
                "[red]No connected accounts found. Please connect your account first.[/red]\n"
            )
            raise typer.Abort(1)

    input_json = {}
    output_json = {}
    input_file_name = DEFAULT_INPUT_FILE_NAME
    output_file_name = DEFAULT_OUTPUT_FILE_NAME

    if import_source == GIT:
        if has_github_provider(accounts):
            # Prompt 4a: Model URL
            model_url = prompt(
                "github repo URL: ",
                validator=Validator.from_callable(validate_url),
            )
            input_json = DEFAULT_INPUT_JSON
            output_json = DEFAULT_OUTPUT_JSON

            config["model_url"] = model_url
            config["provider"] = GITHUB

        else:
            rich.print(
                "No connected Github account found. Please connect your Github account first."
            )
            raise typer.Abort(1)
    # is_serverless = typer.confirm(
    #     "Do you want to deploy on serverless? ", default=False
    # )
    is_serverless = False
    if is_serverless:
        deployment_type = "SERVERLESS"
        gpu_type = prompt(
            "GPU Type (A10) : ",
            completer=get_machine_types_serverless(),
            complete_while_typing=True,
            key_bindings=key_bindings,
            validator=Validator.from_callable(validate_machine_types_serverless),
            validate_while_typing=False,
        )
    else:
        deployment_type = "CONTAINER"
        gpu_type = prompt(
            f"GPU Type ({', '.join(str(x) for x in MACHINE_TYPES)}) : ",
            completer=get_machine_types(),
            complete_while_typing=True,
            key_bindings=key_bindings,
            validator=Validator.from_callable(validate_machine_types),
            validate_while_typing=False,
        )

    is_dedicated = False
    is_custom_runtime = False
    if deployment_type == "CONTAINER":
        print_options("Server type:", MACHINE_TYPE_SERVERS_DEF)
        machine_type_server = prompt(
            "Do you want to use DEDICATED or SHARED server? ",
            completer=get_machine_types_servers(),
            complete_while_typing=True,
            key_bindings=key_bindings,
            validator=Validator.from_callable(validate_machine_types_server),
            validate_while_typing=False,
        )
        is_dedicated = True if machine_type_server == "DEDICATED" else False
        config["configuration"]["is_dedicated"] = is_dedicated
    is_custom_runtime = typer.confirm("Do you have custom runtime? ", default=False)

    if deployment_type == "SERVERLESS":
        is_dedicated = True
        config["configuration"]["is_dedicated"] = True

    # Get default values based on GPU Type and is_dedicated
    default_values = get_default_machine_values(
        gpu_type, "dedicated" if is_dedicated else "shared"
    )

    if is_custom_runtime:
        file_name_full, file_type, file_name = find_requirements_file()
        if file_name_full:
            # File is found
            rich.print(f"\nRequirements file found: {file_name}")
            is_found_file_used = typer.confirm(
                f"Do you want to use {file_name} to load dependencies?", default=True
            )
        else:
            # File is not found
            rich.print("\nNo requirements file automatically detected.")
            is_found_file_used = typer.confirm(
                "Do you want to load dependencies?", default=True
            )

        if is_found_file_used:
            if not file_name_full:
                # Ask the user to specify the file if not automatically found or if they want to specify another file
                file_name_prompt = prompt(
                    "Select your dependency management file: ",
                    default="requirements.txt",
                )
                requirements_file_name = file_name_prompt
                requirements_file_type = file_name_prompt.split(".")[-1]
            else:
                # Use the found file
                requirements_file_name = file_name_full
                requirements_file_type = file_type
        else:
            # User chooses not to load dependencies
            requirements_file_name = None
            requirements_file_type = None

    python_packages = []
    if requirements_file_name:
        if requirements_file_type == "txt":
            python_packages = read_requirements_txt(requirements_file_name)
        elif requirements_file_type == "toml":
            python_packages = read_pyproject_toml(requirements_file_name)

    runtime_config = yaml.load(DEFAULT_INFERLESS_RUNTIME_YAML_FILE)
    # Update runtime config with python packages if any
    if python_packages:
        runtime_config["build"]["python_packages"] = python_packages
        config["optional"]["runtime_file_name"] = DEFAULT_RUNTIME_FILE_NAME
        create_yaml(runtime_config, DEFAULT_RUNTIME_FILE_NAME)
        rich.print(
            f"\n[bold][blue]{DEFAULT_RUNTIME_FILE_NAME}[/bold][/blue] file generated successfully! Also pre-filled `python_packages`. Feel free to modify the file"
        )
        rich.print(
            f"For more information on runtime file, please refer to our docs: [link={RUNTIME_DOCS_URL}]{RUNTIME_DOCS_URL}[/link]"
        )
        rich.print(
            "You can also use [bold][blue]`inferless runtime upload`[/blue][/bold] command to upload runtime\n"
        )
    else:
        # Handle case when no dependencies are loaded
        rich.print("No dependencies specified or loaded.")

    # Prompts for non-serverless options
    # if deployment_type == "CONTAINER":
    config["configuration"]["custom_runtime_id"] = ""
    config["configuration"]["custom_volume_name"] = ""
    config["configuration"]["custom_volume_id"] = ""

    config["configuration"]["min_replica"] = "0"
    config["configuration"]["max_replica"] = "1"
    config["configuration"]["scale_down_delay"] = "600"
    config["optional"]["input_file_name"] = input_file_name
    config["optional"]["output_file_name"] = output_file_name
    config["configuration"]["inference_time"] = "180"
    if deployment_type == "CONTAINER":
        config["configuration"]["is_serverless"] = False
    else:
        config["configuration"]["is_serverless"] = True
    config["configuration"]["gpu_type"] = gpu_type
    config["configuration"]["is_dedicated"] = is_dedicated
    config["configuration"]["vcpu"] = default_values["cpu"]
    config["configuration"]["ram"] = default_values["memory"]
    config["import_source"] = import_source
    config["version"] = "1.0.0"

    create_yaml(config, config_file_name)

    is_input_file_present = is_file_present(input_file_name)
    is_output_file_present = is_file_present(output_file_name)
    is_ioschema_file_present = is_file_present("input_schema.py")
    config["io_schema"] = is_ioschema_file_present
    generate_files = False
    if import_source == "GIT":
        if not is_ioschema_file_present:
            generate_files = not (is_input_file_present and is_output_file_present)

    elif import_source == "LOCAL":
        generate_files = not (is_input_file_present and is_output_file_present)

    if generate_files:
        generate_input_and_output_files(
            input_json,
            output_json,
            input_file_name,
            output_file_name,
        )
        rich.print(
            f"\n[bold][blue]{input_file_name}[/blue][/bold] and [bold][blue]{output_file_name}[/blue][/bold] files generated successfully! Also pre-filled jsons. Feel free to modify the files"
        )
        rich.print(
            f"For more information on input and output json, please refer to our docs: [link={IO_DOCS_URL}]{IO_DOCS_URL}[/link]"
        )
        if import_source == "LOCAL":
            config["io_schema"] = False

    rich.print("\n[green]Initialization completed successfully![/green]\n")
