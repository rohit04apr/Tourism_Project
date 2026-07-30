from huggingface_hub import HfApi, create_repo
from huggingface_hub.utils import RepositoryNotFoundError
import os

api = HfApi(token=os.getenv("HF_TOKEN"))

repo_id = "rohit-tiwari04/wellness-tourism-prediction"
repo_type = "space"

# Step 1: Check if the Space exists, create it if not
try:
    api.repo_info(repo_id=repo_id, repo_type=repo_type)
    print(f"Space '{repo_id}' already exists. Using it.")
except RepositoryNotFoundError:
    print(f"Space '{repo_id}' not found. Creating new space...")
    create_repo(
        repo_id=repo_id,
        repo_type=repo_type,
        space_sdk="docker",  # deployment folder contains a Dockerfile
        private=False,
    )
    print(f"Space '{repo_id}' created.")

# Step 2: Upload deployment files to the Space
api.upload_folder(
    folder_path="tourism_project/deployment",
    repo_id=repo_id,
    repo_type=repo_type,
    path_in_repo="",
)

print("Deployment files successfully uploaded to Hugging Face Space!")