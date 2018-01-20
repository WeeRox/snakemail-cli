"""
usage: snakemail select [<mailbox>]
"""

from mail import imap
from file import read_json, write_json

def run(arguments):
    if '--help' in arguments or '-h' in arguments:
        exit(__doc__.strip())

    if read_json.get_auto_login():
        if len(arguments) > 0:
            status, count = imap.select(arguments[0])
            write_json.set_auto_mailbox(arguments[0])
        else:
            status, count = imap.select()
            write_json.set_auto_mailbox('INBOX')

        if status == 'NO':
            exit("snakemail: there was a problem selecting that inbox, make sure you haven't misspelled the name")
    else:
        exit("snakemail: you are not logged in! To log in, run 'snakemail login <email>'")
