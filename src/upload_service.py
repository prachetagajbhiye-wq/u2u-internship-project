import os


def process_uploaded_file(file):

    upload_folder = "../documents"

    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        folder = "pdf"

    elif filename.endswith(".csv"):
        folder = "csv"

    elif filename.endswith(".json"):
        folder = "json"

    elif filename.endswith(".xlsx"):
        folder = "excel"

    else:
        return {
            "success": False,
            "message": "Unsupported file type."
        }

    destination_folder = os.path.join(upload_folder, folder)

    os.makedirs(destination_folder, exist_ok=True)

    destination = os.path.join(destination_folder, file.filename)

    file.save(destination)

    return {
        "success": True,
        "message": f"{file.filename} uploaded successfully.",
        "filename": file.filename,
        "path": destination
    }