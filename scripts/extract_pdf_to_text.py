import sys
import os
import logging

from azure.ai.formrecognizer import DocumentAnalysisClient
from data_utils import extract_pdf_content, SingletonFormRecognizerClient
from azure.core.credentials import AzureKeyCredential

ip_path = sys.argv[1]
op_dir = sys.argv[2]

logging.basicConfig(level=logging.INFO)

def extract_pdf(ip_fpath, op_fpath):
    logging.info("Processing: %s -> %s", ip_fpath, op_fpath)
    form_rec_resource = "egnyteosharegs"
    form_rec_key = "fc1ab7ea701f4909b8c73a4ff25f1cc4"
    form_recognizer_client = DocumentAnalysisClient(endpoint=f"https://{form_rec_resource}.cognitiveservices.azure.com/", credential=AzureKeyCredential(form_rec_key))

    content = extract_pdf_content(ip_fpath, form_recognizer_client, use_layout=True)

    with open(op_fpath, "w") as f:
        f.write(content)

def main():
    if os.path.isdir(ip_path):
        for fname in os.listdir(ip_path):
            ip_fpath = os.path.join(ip_path, fname)
            if os.path.splitext(ip_fpath)[-1].lower() == ".pdf":
                try:
                    op_fpath = os.path.join(op_dir, os.path.basename(ip_fpath)+".html")
                    if not os.path.exists(op_fpath):
                        extract_pdf(ip_fpath, op_fpath)
                    else:
                        logging.warn("Skipping %s, already exists", ip_fpath)
                except Exception as e:
                    logging.exception(e)
    else:
            op_fpath = os.path.join(op_dir, os.path.basename(ip_path)+".html")
            extract_pdf(ip_path, op_fpath)

main()
