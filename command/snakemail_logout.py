"""
usage: snakemail logout
"""

from file import read_json, write_json
from mail import imap

def run(arguments):
    if '--help' in arguments or '-h' in arguments:
        exit(__doc__.strip())

    if read_json.get_auto_login():
        imap.logout()
        write_json.set_auto_login(None)
