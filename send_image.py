import requests

file_path = "/home/julianc/Wallpapers/karsten-wurth-7BjhtdogU3A-unsplash.jpg"
files = {"file": open(file_path, "rb")}
response = requests.post("https://bookbnb-firebase-test.herokuapp.com/upload_image", files=files)
# aaaaeeeeaaaaa
