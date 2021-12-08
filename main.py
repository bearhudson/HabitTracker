import requests
import time
import os
import inquirer

token = os.environ.get('TOKEN')
username = os.environ.get('USERNAME')
endpoint = "https://pixe.la/v1/users/"

today = time.strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": token,
}

graph_list_names = []
graph_list = []
graph_choice = {}
graph_choice_name = ""
pixel_graphs_endpoint = ""
graph_id = ""


def get_graph_names():
    global graph_list
    pixel_graphs_list = f"{endpoint}{username}/graphs/"
    try:
        req = requests.get(url=pixel_graphs_list, headers=headers)
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)
    graph_list = req.json()
    for graph in graph_list['graphs']:
        graph_list_names.append(graph['name'])


def ask_which_graph():
    global graph_choice
    graph_input = [
        inquirer.List('graph_name', message='Which Graph?', choices=graph_list_names),
    ]
    graph_choice = inquirer.prompt(questions=graph_input)


def get_graph_id():
    global pixel_graphs_endpoint
    global graph_choice_name
    global graph_list
    global graph_id
    graph_choice_name = graph_choice['graph_name']
    for graph in graph_list['graphs']:
        if graph['name'] == graph_choice['graph_name']:
            graph_id = graph['id']
    pixel_graphs_endpoint = f"{endpoint}{username}/graphs/{graph_id}"


def update_graph():
    hours = input("How many hours today? ")
    get_graph_names()
    ask_which_graph()
    get_graph_id()
    payload = {
        "date": today,
        "quantity": hours,
    }
    try:
        requests.post(url=pixel_graphs_endpoint, json=payload, headers=headers)
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)


def delete_graph():
    global graph_id
    get_graph_names()
    ask_which_graph()
    get_graph_id()
    pixel_graphs_delete = f"{endpoint}{username}/graphs/{graph_id}"
    try:
        requests.delete(url=pixel_graphs_delete, headers=headers)
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)


def create_graph():
    global graph_choice_name
    get_graph_names()
    for name in graph_choice_name:
        print(name)
    new_graph_name = input("What's the name of the new graph? ")
    new_graph_id = input("What's the ID of the new graph? ")
    new_unit = input("What is the unit? ")
    new_type = input("What is the type? ")
    new_color = input("What color? [shibafu/momiji/sora/ichou/ajisai/kuro] ")
    pixel_graphs_create = f"{endpoint}{username}/graphs"
    payload = {
        "name": new_graph_name,
        "id": new_graph_id,
        "unit": new_unit,
        "type": new_type,
        "color": new_color
    }
    print(pixel_graphs_create)
    try:
        requests.post(url=pixel_graphs_create, json=payload, headers=headers)
    except requests.exceptions.RequestException as exception:
        raise SystemExit(exception)


delete_graph()
