import fitz
import os

PDF_FOLDER = "../documents"


def load_pdf_text():
    """
    Reads every PDF inside the documents folder
    and combines all text into one string.
    """

    all_text = ""

    if not os.path.exists(PDF_FOLDER):
        return ""

    for file in os.listdir(PDF_FOLDER):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(PDF_FOLDER, file)

            document = fitz.open(pdf_path)

            for page in document:

                all_text += page.get_text()

            document.close()

    return all_text


if __name__ == "__main__":

    text = load_pdf_text()

    print(text[:1000])