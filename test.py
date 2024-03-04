import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "wiki/3", {"subject": "New one", "views": 1000} )
print(response.json())
response = requests.delete(BASE + "wiki/3")
print(response)