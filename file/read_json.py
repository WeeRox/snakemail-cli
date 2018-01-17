import json
import sys, os
from file import write_json

def read(attribute):
    json_data = json.load(config())
    if attribute in json_data:
        return json_data[attribute]
    else:
        return False

def account(email):
    json_data = json.load(config())
    for account in json_data['accounts']:
        if account['email'] == email:
            return account
    return False

def config():
    try:
        file = open(os.path.join(os.path.dirname(sys.argv[0]), ".config"))
    except FileNotFoundError:
        # file was not found, create empty file
        write_json.create()
        file = open(os.path.join(os.path.dirname(sys.argv[0]), ".config"))

    return file
