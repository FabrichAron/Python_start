import json

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = {
    "name": "Ali",
    "age": 20,
    "city": "Moscow"
}



with open("test_1.json", "w") as write_file:
    json.dump(x, write_file, indent=4)




# with open("test_1.json", "r") as r_file:
#     data = json.load(r_file)
# print(f"Mening ismim {data["name"]}, yoshim {data["age"]}. Men {data["city"]}da yashayman.")
