import requests
import time
import os

token = os.environ.get('TOKEN')
username = os.environ.get('USERNAME')
endpoint = "https://pixe.la/v1/users/"

today = time.strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": token,
}

graph_id = "a1"

pixel_endpoint = f"{endpoint}{username}/graphs/{graph_id}"

hours = input("How many hours today? ")

payload = {
    "date": today,
    "quantity": hours,
}

try:
    req = requests.post(url=pixel_endpoint, json=payload, headers=headers)
    print(req.raise_for_status())
except requests.exceptions.RequestException as exception:
    raise SystemExit(exception)
