import json

def load_users(filename="usersfff.json"):
    with open(filename, "r") as file:
        return json.load(file)

users = load_users()
print(users["Doston"]["result"])