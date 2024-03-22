import requests

BASE = "http://172.24.0.3:5000/"

response = requests.put(BASE + "wiki/5", {"subject": "New one", "views": 1000} )
print(response.json())
response = requests.patch(BASE + "wiki/5", {"subject": "new"})
# print(response.json())
# response = requests.get(BASE + "wiki/5")
# print(response.json())