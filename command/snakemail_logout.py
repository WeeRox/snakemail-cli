"""
usage: snakemail logout
"""

from docopt import docopt
from file import read_json, write_json
from mail import imap

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    if read_json.get_auto_login():
        imap.logout()
        write_json.set_auto_login(None)
