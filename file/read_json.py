import json

def get_accounts():
    json_data = json.load(config_file())
    return json_data['accounts']

def get_account(email):
    json_data = json.load(config_file())
    for account in json_data['accounts']:
        if account['email'] == email:
            return account
    return False

def get_auto_login():
    json_data = json.load(config_file())
    return json_data['auto_login']

def get_auto_mailbox():
    json_data = json.load(config_file())
    return json_data['auto_mailbox']

def config_file():
    import sys, os
    try:
        file = open(os.path.join(os.path.dirname(sys.argv[0]), ".config"))
    except FileNotFoundError:
        # file was not found, create empty file
        from file import write_json
        write_json.create()
        file = open(os.path.join(os.path.dirname(sys.argv[0]), ".config"))

    return file
