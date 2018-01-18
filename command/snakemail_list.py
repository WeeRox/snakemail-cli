"""
usage: snakemail list
"""

import docopt
from mail import imap
from file import read_json

def run(arguments):
    arguments = docopt.DocOpt(__doc__).get_args()
    if read_json.get_auto_login():
        status, list = imap.list()
        for x in list:
            print(x)
    else:
        exit('snakemail: you are not logged in!')
