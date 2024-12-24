import json


def load_questions(filename="tests.json"):
    with open(filename, "r") as file:
        return json.load(file)
