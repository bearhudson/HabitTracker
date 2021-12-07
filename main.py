import requests
import time
import os

token = os.environ.get('TOKEN')
username = os.environ.get('USERNAME')
endpoint = "https://pixe.la/v1/users/"

today = time.strftime("%Y%m%d")
print(today)

headers = {
    "X-USER-TOKEN": token,
}

graph_id = "a1"

payload = {
    "date": today,
    "quantity": "1",
}

pixel_endpoint = f"{endpoint}/{username}/graphs/{graph_id}"
req = requests.post(url=pixel_endpoint, json=payload, headers=headers)
print(req.text)
