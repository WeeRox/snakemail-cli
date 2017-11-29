"""
usage: snakemail account add <email>
"""

import docopt

def run():
    arguments = docopt.DocOpt(__doc__).get_args()
    if validate_email(arguments['<email>']):
        print('correct')

def validate_email(email):
    import re
    return re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email);
