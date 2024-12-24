import json


def save_users(users, filename="users.json"):
    with open(filename, "w") as file:
        return json.dump(users, file, indent=4)
