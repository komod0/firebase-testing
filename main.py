import requests
import os
from fastapi import FastAPI, File, UploadFile, Request
from pydantic import BaseModel

from firebase_admin import credentials, initialize_app, storage

app = FastAPI()

client_secret = os.environ.get("FIREBASE-JSON-CERT")
client_secret = json.loads(client_secret)
storage_bucket = os.environ.get("FIREBASE-STORAGE-BUCKET")

# Init firebase with your credentials
cred = credentials.Certificate(client_secret)
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


