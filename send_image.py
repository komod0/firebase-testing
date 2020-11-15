import requests

file_path = "/home/julianc/Wallpapers/ethan-brooke-M2VtwQSkQFs-unsplash.jpg"
files = {"file": open(file_path, "rb")}
response = requests.post("http://localhost:8000/upload_image", files=files)
