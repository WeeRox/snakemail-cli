import json
import sys, os

def create():
    file = open(os.path.join(os.path.dirname(sys.argv[0]), ".config"), "w")
    json_data = {
        "accounts": [],
        "auto_login": None,
        "auto_mailbox": None
    }
    json.dump(json_data, file)

def add_account(email, password, host):
    json_data, file = config_file()
    json_data['accounts'].append({"email": email, "password": password, "host": host})
    json.dump(json_data, file)

def remove_account(email):
    from file import read_json
    account = read_json.get_account(email)

    json_data, file = config_file()
    json_data['accounts'].remove(account)
    json.dump(json_data, file)

def set_auto_login(email):
    json_data, file = config_file()
    json_data['auto_login'] = email
    json.dump(json_data, file)

def set_auto_mailbox(mailbox):
    json_data, file = config_file()
    json_data['auto_mailbox'] = mailbox
    json.dump(json_data, file)

def config_file():
    try:
        file = open(os.path.join(os.path.dirname(sys.argv[0]), ".config"))
    except FileNotFoundError:
        # file was not found, create empty file
        create()
        file = open(os.path.join(os.path.dirname(sys.argv[0]), ".config"))

    return json.load(file), open(os.path.join(os.path.dirname(sys.argv[0]), ".config"), 'w')
