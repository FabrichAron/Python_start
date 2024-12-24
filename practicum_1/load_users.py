import json


def load_users(filename="users.json"):
    with open(filename, "r") as file:
        return json.load(file)
