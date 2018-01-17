import json
import sys, os

def write(attribute, value):
    file = open(os.path.join(os.path.dirname(sys.argv[0]), ".config"), "w")

def create():
    file = open(os.path.join(os.path.dirname(sys.argv[0]), ".config"), "w")
    json_data = {
        "accounts": []
    }
    json.dump(json_data, file)
