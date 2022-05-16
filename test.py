import requests

BASE="http://127.0.0.1:5000/"

response = requests.post(BASE + "video/AE01", {"Name": "Walid", "Views": 300})
print(response.json())
print("------")