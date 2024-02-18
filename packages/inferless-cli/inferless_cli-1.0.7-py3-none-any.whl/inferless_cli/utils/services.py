import os
import rich
import typer
from inferless_cli.utils.api import make_request
from inferless_cli.utils.constants import (
    CREATE_VOLUME_URL,
    DELETE_S3_VOLUME_URL,
    GET_CLI_VERISON_URL,
    GET_CONNECTED_ACCOUNTS_URL,
    GET_MODEL_BUILD_LOGS_URL,
    GET_MODEL_CALL_LOGS_URL,
    GET_S3_PATH_TYPE,
    GET_USER_SECRETS_URL,
    GET_VOLUME_INFO_BY_ID,
    GET_VOLUME_INFO_URL,
    GET_VOLUMES_LIST_URL,
    GET_PREFILLED_IO_URL,
    GET_TEMPLATES_LIST_URL,
    GET_VOLUMES_WORKSPACE_URL,
    GET_VOLUMES_FILES_URL,
    PRESIGNED_URL,
    SAVE_RUNTIME_URL,
    SYNC_S3_TO_NFS,
    SYNC_S3_TO_S3,
    UPDATE_VOLUME_URL,
    VALIDATE_TOKEN_URL,
    GET_WORKSPACES,
    GET_WORKSPACE_MODELS_URL,
    REBUILD_MODEL_URL,
    ACTIVATE_MODEL_URL,
    DEACTIVATE_MODEL_URL,
    DELETE_MODEL_URL,
    IMPORT_MODEL_URL,
    UPLOAD_IO_URL,
    SET_VARIABLES_URL,
    UPDATE_MODEL_CONFIGURATIONS_URL,
    VALIDATE_IMPORT_MODEL_URL,
    START_IMPORT_URL,
    GET_MODEL_CODE_URL,
    INITILIZE_MODEL_UPLOAD_URL,
    GET_SIGNED_URL_FOR_MODEL_UPLOAD_URL,
    COMPLETE_MODEL_UPLOAD_URL,
    GET_MODEL_DETAILS_URL,
    GET_MODEL_FULL_DETAILS_URL,
    VALIDATE_GITHUB_URL_PERMISIONS_URL,
)
from inferless_cli import __version__
from rich.progress import Progress
from inferless_cli.utils.helpers import (
    decrypt_cli_key,
    decrypt_tokens,
    save_tokens,
    validate_jwt,
)


def get_connected_accounts(import_source):
    payload = {
        "import_source": import_source,
    }

    response = make_request(
        GET_CONNECTED_ACCOUNTS_URL, method="POST", auth=True, data=payload
    )

    return response.json()["details"]


def get_workspaces_list():
    response = make_request(GET_WORKSPACES, method="POST", auth=True)

    return response.json()["details"]


# !not used
def get_prefilled_io(task_type):
    payload = {"task_type": task_type}

    response = make_request(
        GET_PREFILLED_IO_URL, method="POST", auth=True, data=payload
    )

    response_json = response.json()

    if "details" not in response_json:
        api_message = response_json["message"]
        rich.print(f"Failed to get data from API. Message: {api_message}")

    return response_json["details"]


def get_volumes_list(workspace_id: str):
    payload = {"workspace_id": workspace_id}

    response = make_request(
        GET_VOLUMES_LIST_URL, method="POST", auth=True, data=payload
    )

    if not response.json().get("details"):
        rich.print("No details in response")

    return response.json()["details"]


def get_volume_info(workspace_id: str, name: str, region: str):
    payload = {"workspace_id": workspace_id, "volume_name": name, "region": region}

    response = make_request(GET_VOLUME_INFO_URL, method="POST", auth=True, data=payload)

    if not response.json().get("details"):
        rich.print("No details in response")

    return response.json()["details"]


def get_volume_info_with_id(workspace_id: str, id: str):
    payload = {"workspace_id": workspace_id, "volume_id": id}

    response = make_request(
        GET_VOLUME_INFO_BY_ID, method="POST", auth=True, data=payload
    )

    if not response.json().get("details"):
        rich.print("No details in response")

    return response.json()["details"]


def create_volume(workspace_id: str, name: str, region: str):
    payload = {
        "workspace_id": workspace_id,
        "name": name,
        "region": region,
    }

    response = make_request(CREATE_VOLUME_URL, method="POST", auth=True, data=payload)

    if not response.json().get("details"):
        rich.print("No details in response")

    return response.json()["details"]


def get_templates_list(workspace_id: str):
    payload = {"workspace_id": workspace_id}

    response = make_request(
        GET_TEMPLATES_LIST_URL, method="POST", auth=True, data=payload
    )

    response_json = response.json()

    return response_json["details"]


def create_presigned_url(payload, uuid, name, file_name, path, workspace_id):
    response = make_request(PRESIGNED_URL, method="POST", auth=True, data=payload)

    data = response.json()
    if data:
        return upload_runtime(
            data["details"], uuid, name, file_name, path, workspace_id
        )


def create_presigned_download_url(payload):
    response = make_request(PRESIGNED_URL, method="POST", auth=True, data=payload)

    response_json = response.json()

    return response_json["details"]
    # data = response.json()
    # if data:
    #     return get_file_download(data["details"])


def create_presigned_upload_url(payload, path):
    response = make_request(PRESIGNED_URL, method="POST", auth=True, data=payload)

    data = response.json()
    if data:
        return upload_volume_file(data["details"], path)


def delete_volume_files_url(payload):
    response = make_request(
        DELETE_S3_VOLUME_URL, method="POST", auth=True, data=payload
    )
    if not response.json().get("details"):
        rich.print("No details in response")

    return response.json()["details"]


def delete_volume_file(url):
    response = make_request(
        url,
        method="DELETE",
        auth=False,
        convert_json=False,
    )
    if response.status_code == 204:
        return {
            "status": "success",
        }


def upload_volume_file(url, path):
    file_size = os.path.getsize(path)
    # file_name = os.path.basename(path)
    # with Progress() as progress:
    #     task = progress.add_task(f"Uploading {file_name} :", total=file_size)
    rich.print(f"Uploading {path}")
    with open(path, "rb") as file:
        # while not progress.finished:
        #     chunk = file.read(4096)
        #     if not chunk:
        #         break
        response = make_request(
            url,
            method="PUT",
            data="" if file_size == 0 else file,
            auth=False,
            convert_json=False,
        )
        if response.status_code != 200:
            raise Exception(f"Upload failed with status code {response.status_code}")
        # progress.update(task, advance=len(chunk))
        if response.status_code == 200:
            return {
                "status": "success",
            }


def get_file_download(url):
    response = make_request(
        url,
        method="GET",
        auth=False,
        convert_json=False,
    )
    return response


def upload_runtime(url, uuid, name, file_name, path, workspace_id):
    with open(path, "rb") as file:
        headers = {
            "Content-Type": "application/x-yaml",
            "x-amz-acl": "bucket-owner-full-control",
        }
        response = make_request(
            url,
            method="PUT",
            data=file,
            auth=False,
            headers=headers,
            convert_json=False,
        )
        if response.status_code == 200:
            return save_runtime(
                {
                    "workspace_id": workspace_id,
                    "name": name,
                    "template_url": f"{uuid}/{file_name}",
                }
            )


def save_runtime(payload):
    response = make_request(SAVE_RUNTIME_URL, method="POST", auth=True, data=payload)

    return response.json()["details"]


def validate_cli_token(key, secret):
    payload = {"access_key": key, "secret_key": secret}
    headers = {"Content-Type": "application/json"}

    response = make_request(
        VALIDATE_TOKEN_URL, method="POST", headers=headers, auth=False, data=payload
    )

    return response.json()["details"]


def callback_with_auth_validation():
    min_version_required()
    get_auth_validation()


def get_auth_validation():
    error_statement = "[red]Please login to Inferless using `inferless login`[/red]"
    token, _, user_id, workspace_id, workspace_name = decrypt_tokens()
    key, secret = decrypt_cli_key()
    if not key or not secret:
        rich.print(error_statement)
        raise typer.Exit(1)
    if token is None:
        rich.print(error_statement)
        raise typer.Exit(1)
    if not validate_jwt(token):
        details = validate_cli_token(key, secret)
        if details["access"] and details["refresh"]:
            save_tokens(
                details["access"],
                details["refresh"],
                user_id,
                workspace_id,
                workspace_name,
            )


def min_version_required():
    error_statement = "Please update Inferless CLI using [bold][red]`pip install inferless-cli --upgrade`[/red][/bold] \n\n"
    version = get_latest_version()

    errmsg, error = compare_versions(__version__, version)
    if error:
        rich.print(f"{errmsg} \n\n{error_statement}")
        raise typer.Exit(1)


def compare_versions(current_version, latest_version):
    current_components = list(map(int, current_version.split(".")))
    latest_components = list(map(int, latest_version.split(".")))

    # Pad the shorter version with zeros to ensure equal length
    while len(current_components) < len(latest_components):
        current_components.append(0)
    while len(latest_components) < len(current_components):
        latest_components.append(0)

    # Compare each component
    for current, latest in zip(current_components, latest_components):
        if current < latest:
            return (
                f"\ncurrent version ([blue]{current_version}[/blue]) is older than minimum required version ([blue]{latest_version}[/blue])",
                True,
            )
        elif current > latest:
            return f"{current_version} is newer than {latest_version}", False

    return f"{current_version} is the same as {latest_version}", False


# !  Not used
def get_min_version_required():
    response = make_request(GET_CLI_VERISON_URL, method="POST", auth=True)
    return response.json()["details"]


def get_latest_version():
    response = make_request(
        "https://pypi.org/pypi/inferless-cli/json", method="GET", auth=False
    )
    return response.json()["info"]["version"]


def get_workspace_models(workspace_id, filter="NONE"):
    payload = {
        "filter_by": filter,
        "search": "",
        "sort_by": "-updated_at",
        "workspace_id": workspace_id,
    }
    response = make_request(
        GET_WORKSPACE_MODELS_URL, method="POST", auth=True, data=payload
    )

    return response.json()["details"]


def rebuild_model(model_id):
    payload = {
        "id": model_id,
    }
    response = make_request(REBUILD_MODEL_URL, method="POST", auth=True, data=payload)

    return response.json()["details"]


def delete_model(model_id):
    payload = {
        "model_id": model_id,
    }
    response = make_request(DELETE_MODEL_URL, method="POST", auth=True, data=payload)

    return response.json()["details"]


def activate_model(model_id):
    payload = {
        "min_replica": 0,
        "max_replica": 1,
        "model_id": model_id,
    }
    response = make_request(ACTIVATE_MODEL_URL, method="POST", auth=True, data=payload)

    return response.json()["details"]


def deactivate_model(model_id):
    payload = {
        "min_replica": 0,
        "max_replica": 0,
        "model_id": model_id,
    }
    response = make_request(
        DEACTIVATE_MODEL_URL, method="POST", auth=True, data=payload
    )

    return response.json()["details"]


def import_model(data):
    response = make_request(IMPORT_MODEL_URL, method="POST", auth=True, data=data)

    return response.json()["details"]


def upload_io(data):
    response = make_request(UPLOAD_IO_URL, method="POST", auth=True, data=data)

    return response.json()["details"]


def update_model_configuration(data):
    response = make_request(
        UPDATE_MODEL_CONFIGURATIONS_URL, method="POST", auth=True, data=data
    )

    return response.json()["details"]


def validate_import_model(data):
    response = make_request(
        VALIDATE_IMPORT_MODEL_URL, method="POST", auth=True, data=data
    )

    return response.json()["details"]


def set_env_variables(data):
    response = make_request(SET_VARIABLES_URL, method="POST", auth=True, data=data)

    return response.json()["details"]


def start_import_model(data):
    response = make_request(START_IMPORT_URL, method="POST", auth=True, data=data)

    return response.json()["details"]


def get_model_import_details(id):
    response = make_request(
        f"{GET_MODEL_DETAILS_URL}/{id}/get/", method="GET", auth=True
    )

    return response.json()["details"]


def get_model_code(id):
    payload = {
        "model_id": id,
    }
    response = make_request(
        f"{GET_MODEL_CODE_URL}", method="POST", auth=True, data=payload
    )

    return response.json()["details"]


def get_model_details(id):
    payload = {
        "model_id": id,
    }
    response = make_request(
        f"{GET_MODEL_FULL_DETAILS_URL}", method="POST", auth=True, data=payload
    )
    return response.json()["details"]


def get_user_secrets():
    payload = {}
    response = make_request(
        f"{GET_USER_SECRETS_URL}", method="POST", auth=True, data=payload
    )
    return response.json()["details"]


def validate_github_url_permissions(url):
    payload = {
        "url": url,
    }
    response = make_request(
        VALIDATE_GITHUB_URL_PERMISIONS_URL, method="POST", auth=True, data=payload
    )

    return response.json()["details"]


def initialize_model_upload(key):
    payload = {
        "key": key,
    }
    response = make_request(
        INITILIZE_MODEL_UPLOAD_URL, method="POST", auth=True, data=payload
    )

    return response.json()


def get_signed_url_for_model_upload(key, upload_id, no_of_parts):
    payload = {
        "key": key,
        "upload_id": upload_id,
        "no_of_parts": no_of_parts,
    }
    response = make_request(
        GET_SIGNED_URL_FOR_MODEL_UPLOAD_URL, method="POST", auth=True, data=payload
    )

    return response.json()


def complate_model_upload(key, upload_id, parts):
    payload = {
        "key": key,
        "upload_id": upload_id,
        "parts": parts,
    }
    response = make_request(
        COMPLETE_MODEL_UPLOAD_URL, method="POST", auth=True, data=payload
    )

    return response


def upload_file(selected_file, key):
    if selected_file:
        initialize_data = initialize_model_upload(key)
        if initialize_data.get("status") == "success" and initialize_data.get(
            "details", {}
        ).get("upload_id"):
            chunk_size = 50 * 1024 * 1024  # 50 MiB
            chunk_count = (selected_file.tell() // chunk_size) + 1

            signed_url_data = get_signed_url_for_model_upload(
                key, initialize_data["details"]["upload_id"], chunk_count
            )

            signed_urls = signed_url_data.get("details", {}).get("urls", [])
            multi_upload_array = []

            for upload_count in range(1, chunk_count + 1):
                file_blob = (
                    selected_file.read(chunk_size)
                    if upload_count < chunk_count
                    else selected_file.read()
                )

                pre_signed_url = signed_urls[upload_count - 1].get("signed_url", "")
                if pre_signed_url:
                    headers = {"Content-Type": "application/zip"}
                    upload_response = make_request(
                        pre_signed_url,
                        method="PUT",
                        data=file_blob,
                        auth=False,
                        headers=headers,
                        convert_json=False,
                    )
                    if upload_response.status_code == 200:
                        multi_upload_array.append(
                            {
                                "PartNumber": upload_count,
                                "ETag": upload_response.headers.get("etag").replace(
                                    '"', ""
                                ),
                            }
                        )
            if multi_upload_array:
                complete_response = complate_model_upload(
                    key, initialize_data["details"]["upload_id"], multi_upload_array
                )

                if complete_response.status_code == 200:
                    return signed_urls[0]["signed_url"].split("?")[0]

    return None


def get_build_logs(payload):
    response = make_request(
        f"{GET_MODEL_BUILD_LOGS_URL}", method="POST", auth=True, data=payload
    )
    return response.json()


def get_call_logs(payload):
    response = make_request(
        f"{GET_MODEL_CALL_LOGS_URL}", method="POST", auth=True, data=payload
    )
    return response.json()


def get_volume_files(payload):
    response = make_request(
        f"{GET_VOLUMES_FILES_URL}", method="POST", auth=True, data=payload
    )
    return response.json()


def update_volume(payload):
    response = make_request(
        f"{UPDATE_VOLUME_URL}", method="POST", auth=True, data=payload
    )
    return response.json()


def get_s3_path_type(payload):
    response = make_request(
        f"{GET_S3_PATH_TYPE}", method="POST", auth=True, data=payload
    )
    return response.json()


def sync_s3_to_nfs(payload):
    response = make_request(f"{SYNC_S3_TO_NFS}", method="POST", auth=True, data=payload)
    return response.json()


def sync_s3_to_s3(payload):
    response = make_request(f"{SYNC_S3_TO_S3}", method="POST", auth=True, data=payload)
    return response.json()
