import json
import os

from fastapi import FastAPI, File, UploadFile
from firebase_admin import credentials, initialize_app, storage

app = FastAPI()

storage_bucket = os.environ.get("FIREBASE-STORAGE-BUCKET")

# Init firebase with your credentials
cred = credentials.Certificate(
{
  "type": "service_account",
  "project_id": os.environ.get("FIREBASE-PROJECT-ID"),
  "private_key_id": os.environ.get("FIREBASE-PRIVATE-KEY-ID"),
  "private_key": os.environ.get("FIREBASE-PRIVATE-KEY").replace('\\n', '\n'),
  "client_email": os.environ.get("FIREBASE-CLIENT-EMAIL"),
  "client_id": os.environ.get("FIREBASE-CLIENT-ID"),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.environ.get("FIREBASE-CLIENT-CERT-URL")
}
    )

initialize_app(cred, {'storageBucket': storage_bucket})


@app.post("/upload_image")
async def root(file: UploadFile = File(...)):
    # Put your local file path
    file_name = file.filename
    bucket = storage.bucket()
    blob = bucket.blob(file_name)
    blob.upload_from_file(file.file)

    # Opt : if you want to make public access from the URL
    blob.make_public()
    print("your file url", blob.public_url)
