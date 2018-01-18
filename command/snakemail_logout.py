"""
usage: snakemail logout
"""

import docopt
from file import read_json, write_json
from mail import imap

def run(arguments):
    arguments = docopt.DocOpt(__doc__).get_args()
    if read_json.get_auto_login():
        imap.logout()
        write_json.set_auto_login(None)
