import json

with open("virtual_machines.json", "r") as file:
    data = json.load(file)
    print(data)