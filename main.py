import json
import os

from fastapi import FastAPI, File, UploadFile
from firebase_admin import credentials, initialize_app, storage

app = FastAPI()

client_secret_raw = os.environ["FIREBASE-JSON-CERT"].replace('\\n', '\n')
print(fr"{client_secret_raw}")
client_secret = json.loads(client_secret_raw)
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
