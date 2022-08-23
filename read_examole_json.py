import json


def read_example_json():
    with open("message_example.json", 'r') as f:
        data = json.load(f)
    return data
