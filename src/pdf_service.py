import fitz
import os


def load_pdfs(folder="../documents/pdf"):
    """
    Reads every PDF inside the folder.
    Returns a list of dictionaries.
    """

    documents = []

    if not os.path.exists(folder):
        return documents

    for filename in os.listdir(folder):

        if not filename.endswith(".pdf"):
            continue

        path = os.path.join(folder, filename)

        pdf = fitz.open(path)

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()

        documents.append({
            "text": text,
            "source": filename
        })

    return documents