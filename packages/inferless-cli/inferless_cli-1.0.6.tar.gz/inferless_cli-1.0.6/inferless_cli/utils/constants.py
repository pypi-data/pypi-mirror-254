# Base constants used in the CLI
import keyring

select_url = lambda url_dev, url_prod, mode: url_dev if mode == "DEV" else url_prod

mode = keyring.get_password("Inferless", "mode")

BASE_URL_PROD = "https://api.inferless.com/api"
WEB_URL_PROD = "https://console.inferless.com"

BASE_URL_DEV = "https://devapi.inferless.com/api"
WEB_URL_DEV = "https://console-dev.inferless.com"

BASE_URL = select_url(BASE_URL_DEV, BASE_URL_PROD, mode)
WEB_URL = select_url(WEB_URL_DEV, WEB_URL_PROD, mode)

DOCS_URL = "https://docs.inferless.com"

# Browser endpoints
CLI_AUTH_URL = f"{WEB_URL}/user/keys"
IO_DOCS_URL = "https://docs.inferless.com/model-import/input-output-json"
RUNTIME_DOCS_URL = "https://docs.inferless.com/model-import/bring-custom-packages"


# API endpoints
GET_CONNECTED_ACCOUNTS_URL = f"{BASE_URL}/accounts/list/connected/"
GET_PREFILLED_IO_URL = f"{BASE_URL}/model_import/huggingface/prefill"
GET_VOLUMES_LIST_URL = f"{BASE_URL}/volumes/list/"
GET_VOLUME_INFO_URL = f"{BASE_URL}/volumes/fetch_volume_details_with_name/"
GET_VOLUME_INFO_BY_ID = f"{BASE_URL}/volumes/fetch_volume_details_with_id/"
CREATE_VOLUME_URL = f"{BASE_URL}/volumes/create/"
DELETE_S3_VOLUME_URL = f"{BASE_URL}/volumes/s3-delete/"
GET_S3_PATH_TYPE = f"{BASE_URL}/s3-path-type/"
SYNC_S3_TO_NFS = f"{BASE_URL}/volumes/s3-nfs-sync/"
SYNC_S3_TO_S3 = f"{BASE_URL}/volumes/s3-to-s3-sync/"
GET_TEMPLATES_LIST_URL = f"{BASE_URL}/workspace/models/templates/list/"
GET_WORKSPACE_MODELS_URL = f"{BASE_URL}/workspace/models/list/"
DELETE_MODEL_URL = f"{BASE_URL}/workspace/models/delete/"
DEACTIVATE_MODEL_URL = f"{BASE_URL}/models/deactivate/"
REBUILD_MODEL_URL = f"{BASE_URL}/model_import/rebuild_model/"
ACTIVATE_MODEL_URL = f"{BASE_URL}/models/activate/"
VALIDATE_TOKEN_URL = f"{BASE_URL}/cli-tokens/exchange/"
GET_WORKSPACES = f"{BASE_URL}/workspace/list"
IMPORT_MODEL_URL = f"{BASE_URL}/model_import/create_update/"
UPLOAD_IO_URL = f"{BASE_URL}/model_import/model_input_output_files/"
UPDATE_MODEL_CONFIGURATIONS_URL = f"{BASE_URL}/model_import/model_configuration/"
START_IMPORT_URL = f"{BASE_URL}/model_import/start_import/"
GET_MODEL_DETAILS_URL = f"{BASE_URL}/model_import"
GET_MODEL_FULL_DETAILS_URL = f"{BASE_URL}/workspace/models/details/"
GET_USER_SECRETS_URL = f"{BASE_URL}/users/secrets/list/"
GET_VOLUMES_WORKSPACE_URL = f"{BASE_URL}/users/secrets/list/"
GET_VOLUMES_FILES_URL = f"{BASE_URL}/volumes/files/"
UPDATE_VOLUME_URL = f"{BASE_URL}/volumes/update/"
GET_MODEL_BUILD_LOGS_URL = f"{BASE_URL}/models/logs/build/v2/"
GET_MODEL_CALL_LOGS_URL = f"{BASE_URL}/models/logs/inference/v2/"
GET_MODEL_CODE_URL = f"{BASE_URL}/models/code/"
VALIDATE_IMPORT_MODEL_URL = f"{BASE_URL}/model_import/validate_model/"
VALIDATE_GITHUB_URL_PERMISIONS_URL = f"{BASE_URL}/model_import/check_git_permission/"
SET_VARIABLES_URL = f"{BASE_URL}/model_import/enviornment/update/"
INITILIZE_MODEL_UPLOAD_URL = (
    f"{BASE_URL}/model_import/uploads/initializeMultipartUpload/"
)
GET_SIGNED_URL_FOR_MODEL_UPLOAD_URL = (
    f"{BASE_URL}/model_import/uploads/getMultipartPreSignedUrls/"
)
COMPLETE_MODEL_UPLOAD_URL = f"{BASE_URL}/model_import/uploads/finalizeMultipartUpload/"
PRESIGNED_URL = f"{BASE_URL}/users/presigned-url"
SAVE_RUNTIME_URL = f"{BASE_URL}/workspace/models/templates/create_update/"
GET_CLI_VERISON_URL = f"{BASE_URL}/cli-app/version/get/"

# UI/UX constants
FRAMEWORKS = ["ONNX", "TENSORFLOW", "PYTORCH"]
DEPLOYMENT_TYPE = ["CONTAINER", "SERVERLESS"]
UPLOAD_METHODS = ["GIT", "LOCAL"]
MACHINE_TYPES = ["A100", "T4"]
MACHINE_TYPES_SERVERLESS = ["A10"]
REGION_TYPES = ["AZURE", "AWS", "SERVERLESS_AWS"]
MACHINE_TYPE_SERVERS = ["SHARED", "DEDICATED"]
MACHINE_TYPE_SERVERS_DEF = [
    "SHARED - Efficiently running on half the capacity for optimal resource sharing.",
    "DEDICATED - Maximizing performance with full resource allocation.",
]
HF_TASK_TYPE = [
    {
        "id": "audio-classification",
        "value": "audio-classification",
        "display_name": "Audio Classification",
        "task_category": "transformer",
    },
    {
        "id": "automatic-speech-recognition",
        "value": "automatic-speech-recognition",
        "display_name": "Automatic Speech Recognition",
        "task_category": "transformer",
    },
    {
        "id": "conversational",
        "value": "conversational",
        "display_name": "Conversational",
        "task_category": "transformer",
    },
    {
        "id": "depth-estimation",
        "value": "depth-estimation",
        "display_name": "Depth Estimation",
        "task_category": "transformer",
    },
    {
        "id": "Depth-to-Image",
        "value": "Depth-to-Image",
        "display_name": "Depth-to-Image",
        "task_category": "diffuser",
    },
    {
        "id": "document-question-answering",
        "value": "document-question-answering",
        "display_name": "Document Question Answering",
        "task_category": "transformer",
    },
    {
        "id": "feature-extraction",
        "value": "feature-extraction",
        "display_name": "Feature Extraction",
        "task_category": "transformer",
    },
    {
        "id": "fill-mask",
        "value": "fill-mask",
        "display_name": "Fill Mask",
        "task_category": "transformer",
    },
    {
        "id": "image-classification",
        "value": "image-classification",
        "display_name": "Image Classification",
        "task_category": "transformer",
    },
    {
        "id": "image-segmentation",
        "value": "image-segmentation",
        "display_name": "Image Segmentation",
        "task_category": "transformer",
    },
    {
        "id": "image-to-text",
        "value": "image-to-text",
        "display_name": "Image To Text",
        "task_category": "transformer",
    },
    {
        "id": "Image-Variation",
        "value": "Image-Variation",
        "display_name": "Image-Variation",
        "task_category": "diffuser",
    },
    {
        "id": "Image-to-Image",
        "value": "Image-to-Image",
        "display_name": "Image-to-Image",
        "task_category": "diffuser",
    },
    {
        "id": "Inpaint",
        "value": "Inpaint",
        "display_name": "Inpaint",
        "task_category": "diffuser",
    },
    {
        "id": "InstructPix2Pix",
        "value": "InstructPix2Pix",
        "display_name": "InstructPix2Pix",
        "task_category": "diffuser",
    },
    {
        "id": "object-detection",
        "value": "object-detection",
        "display_name": "Object Detection",
        "task_category": "transformer",
    },
    {
        "id": "question-answering",
        "value": "question-answering",
        "display_name": "Question Answering",
        "task_category": "transformer",
    },
    {
        "id": "Stable-Diffusion-Latent-Upscaler",
        "value": "Stable-Diffusion-Latent-Upscaler",
        "display_name": "Stable-Diffusion-Latent-Upscaler",
        "task_category": "diffuser",
    },
    {
        "id": "summarization",
        "value": "summarization",
        "display_name": "Summarization",
        "task_category": "transformer",
    },
    {
        "id": "Super-Resolution",
        "value": "Super-Resolution",
        "display_name": "Super-Resolution",
        "task_category": "diffuser",
    },
    {
        "id": "table-question-answering",
        "value": "table-question-answering",
        "display_name": "Table Question Answering",
        "task_category": "transformer",
    },
    {
        "id": "text-classification",
        "value": "text-classification",
        "display_name": "Text Classification",
        "task_category": "transformer",
    },
    {
        "id": "text-generation",
        "value": "text-generation",
        "display_name": "Text Generation",
        "task_category": "transformer",
    },
    {
        "id": "Text-to-Image",
        "value": "Text-to-Image",
        "display_name": "Text-to-Image",
        "task_category": "diffuser",
    },
    {
        "id": "text2text-generation",
        "value": "text2text-generation",
        "display_name": "Text2text Generation",
        "task_category": "transformer",
    },
    {
        "id": "token-classification",
        "value": "token-classification",
        "display_name": "Token Classification",
        "task_category": "transformer",
    },
    {
        "id": "translation",
        "value": "translation",
        "display_name": "Translation",
        "task_category": "transformer",
    },
    {
        "id": "video-classification",
        "value": "video-classification",
        "display_name": "Video Classification",
        "task_category": "transformer",
    },
    {
        "id": "visual-question-answering",
        "value": "visual-question-answering",
        "display_name": "Visual Question Answering",
        "task_category": "transformer",
    },
    {
        "id": "zero-shot-audio-classification",
        "value": "zero-shot-audio-classification",
        "display_name": "Zero Shot Audio Classification",
        "task_category": "transformer",
    },
    {
        "id": "zero-shot-classification",
        "value": "zero-shot-classification",
        "display_name": "Zero Shot Classification",
        "task_category": "transformer",
    },
    {
        "id": "zero-shot-image-classification",
        "value": "zero-shot-image-classification",
        "display_name": "Zero Shot Image Classification",
        "task_category": "transformer",
    },
    {
        "id": "zero-shot-object-detection",
        "value": "zero-shot-object-detection",
        "display_name": "Zero Shot Object Detection",
        "task_category": "transformer",
    },
]
HUGGINGFACE_TYPE = [
    {"id": "transformer", "value": "transformer", "display_name": "Transformer"},
    {"id": "diffuser", "value": "diffuser", "display_name": "Diffuser"},
]
GITHUB = "GITHUB"
HUGGINGFACE = "HUGGINGFACE"
GIT = "GIT"


APP_PY = "app.py"
MODEL_ONNX = "model.onnx"
DEFAULT_YAML_FILE_NAME = "inferless.yaml"
DEFAULT_INPUT_JSON = {
    "inputs": [
        {
            "data": ["Once upon a time"],
            "name": "prompt",
            "shape": [1],
            "datatype": "BYTES",
        }
    ]
}
DEFAULT_OUTPUT_JSON = {
    "outputs": [
        {
            "data": [
                "Once upon a time the sun was up he would look down to the valley below and wonder wis"
            ],
            "name": "generated_text",
            "shape": [1],
            "datatype": "BYTES",
        }
    ]
}
DEFAULT_INPUT_FILE_NAME = "input.json"
DEFAULT_OUTPUT_FILE_NAME = "output.json"
DEFAULT_RUNTIME_FILE_NAME = "inferless-runtime-config.yaml"
DEFAULT_MACHINE_VALUES = {
    "shared": {
        "T4": {
            "min_cpu": "1.5",
            "max_cpu": "1.5",
            "cpu": "1.5",
            "memory": "10",
            "min_memory": "10",
            "max_memory": "10",
        },
        "A100": {
            "min_cpu": "10",
            "max_cpu": "10",
            "cpu": "10",
            "memory": "100",
            "min_memory": "100",
            "max_memory": "100",
        },
        "A10": {
            "min_cpu": "3",
            "max_cpu": "3",
            "cpu": "3",
            "memory": "15",
            "min_memory": "15",
            "max_memory": "15",
        },
    },
    "dedicated": {
        "T4": {
            "min_cpu": "3",
            "max_cpu": "3",
            "cpu": "3",
            "memory": "20",
            "min_memory": "20",
            "max_memory": "20",
        },
        "A100": {
            "min_cpu": "20",
            "max_cpu": "20",
            "cpu": "20",
            "memory": "200",
            "min_memory": "200",
            "max_memory": "200",
        },
        "A10": {
            "min_cpu": "7",
            "max_cpu": "7",
            "cpu": "7",
            "memory": "30",
            "min_memory": "30",
            "max_memory": "30",
        },
    },
}


DEFAULT_INFERLESS_YAML_FILE = """\
# Inferless config file (version: 1.0.0)
version: 1.0.0

name: TEST
import_source: GIT

# you can choose the options between ONNX, TENSORFLOW, PYTORCH
source_framework_type: PYTORCH

configuration:
  # if you want to use a custom runtime, add the runtime id below.
  # you can find it by running `inferless runtime list` or create one with `inferless runtime upload` and update this file it by running `inferless runtime select --id <RUNTIME_ID>`.
  custom_runtime_id: ''

  # if you want to use a custom volume, add the volume id and name below,
  # you can find it by running `inferless volume list` or create one with `inferless volume create -n {VOLUME_NAME}`
  custom_volume_id: ''
  custom_volume_name: ''

  gpu_type: T4
  inference_time: '180'
  is_dedicated: false
  is_serverless: true
  max_replica: '1'
  min_replica: '1'
  scale_down_delay: '600'
env:
  # Add your environment variables here
  # ENV: 'PROD'
secrets:
  # Add your secret ids here you can find it by running `inferless secrets list`
  # - 65723205-ce21-4392-a10b-3tf00c58988c
optional:
  # you can update file names here
  input_file_name: input.json
  output_file_name: output.json
"""


DEFAULT_INFERLESS_RUNTIME_YAML_FILE = """\
build:
  # cuda_version: we currently support 12.1.1 and 11.8.0.
  cuda_version: 12.1.1
  python_packages:
    # you can add more python packages here
  system_packages:
    # - "libssl-dev" #example
    # you can add system packages here
"""

GLITCHTIP_DSN = "https://7d9a4e0478da4efaa34b1f5c8191b820@app.glitchtip.com/5058"
