from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="tourism_project/deployment",
    repo_id="rohit-tiwari04/wellness-tourism-prediction",
    repo_type="space",
    path_in_repo="",
)

print("Deployment files successfully uploaded to Hugging Face Space!")
