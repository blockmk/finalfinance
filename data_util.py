import json

def load_finance(): 
    with open('data.json', 'r') as file:
        return json.load(file)

def write_finance(e):
    with open('data.json', 'w') as file:
        json.dump(e, file, indent=4)

