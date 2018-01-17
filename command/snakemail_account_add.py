"""
usage: snakemail account add <email>
"""

import docopt

def run():
    arguments = docopt.DocOpt(__doc__).get_args()
    if validate_email(arguments['<email>']):
        from file import read_json
        account = read_json.account(arguments['<email>'])
        if account:
            print("This account has already been registered!")
        else:
            # TODO: initiate regsitration process

def validate_email(email):
    import re
    return re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email);
