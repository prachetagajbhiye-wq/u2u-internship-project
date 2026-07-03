import os
import json
import pandas as pd
import fitz

DOCUMENTS_FOLDER = "../documents"


def load_documents():

    documents = []

    # ---------------- CSV ----------------

    csv_folder = os.path.join(DOCUMENTS_FOLDER, "csv")

    if os.path.exists(csv_folder):

        for file in os.listdir(csv_folder):

            if file.endswith(".csv"):

                path = os.path.join(csv_folder, file)

                df = pd.read_csv(path)

                for _, row in df.iterrows():

                    text = " | ".join(str(value) for value in row.values)

                    documents.append({
                        "text": text,
                        "source": file
                    })

    # ---------------- PDF ----------------

    pdf_folder = os.path.join(DOCUMENTS_FOLDER, "pdf")

    if os.path.exists(pdf_folder):

        for file in os.listdir(pdf_folder):

            if file.endswith(".pdf"):

                path = os.path.join(pdf_folder, file)

                pdf = fitz.open(path)

                text = ""

                for page in pdf:
                    text += page.get_text()

                pdf.close()

                documents.append({
                    "text": text,
                    "source": file
                })

    # ---------------- JSON ----------------

    json_folder = os.path.join(DOCUMENTS_FOLDER, "json")

    if os.path.exists(json_folder):

        for file in os.listdir(json_folder):

            if file.endswith(".json"):

                path = os.path.join(json_folder, file)

                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                documents.append({
                    "text": json.dumps(data, indent=2),
                    "source": file
                })

    # ---------------- Excel ----------------

    excel_folder = os.path.join(DOCUMENTS_FOLDER, "excel")

    if os.path.exists(excel_folder):

        for file in os.listdir(excel_folder):

            if file.endswith(".xlsx"):

                path = os.path.join(excel_folder, file)

                df = pd.read_excel(path)

                for _, row in df.iterrows():

                    documents.append({
                        "text": " | ".join(str(v) for v in row.values),
                        "source": file
                    })

    return documents