import requests

BASE="http://127.0.0.1:5000/"

response = requests.post(BASE + "video/AE01", {"Name": "Walid", "Views": 300, "Likes": 70})
print(response.json())

input()

response = requests.get(BASE + "video/AE01")
print(response.json())

input()

response = requests.delete(BASE + "video/AE01")
print(response)

input()

response = requests.get(BASE + "video/AE01")
print(response.json())
