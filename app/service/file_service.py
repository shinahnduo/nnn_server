import os
from app.repository.file_repository import upload_to_dropbox, get_dropbox_file_link

def save_image_to_dropbox(file, temp_dir: str = "temp") -> str:
    try:
        os.makedirs(temp_dir, exist_ok=True)

        local_path = os.path.join(temp_dir, file.filename)
        with open(local_path, "wb") as f:
            f.write(file.file.read())

        dropbox_path = f"/uploads/{file.filename}"

        uploaded_path = upload_to_dropbox(local_path, dropbox_path)

        os.remove(local_path)

        return uploaded_path
    except Exception as e:
        raise

def get_image_link_from_dropbox(dropbox_path: str) -> str:
    try:
        return get_dropbox_file_link(dropbox_path)
    except Exception as e:
        raise