"""
usage: snakemail search [<query>]
"""

import regex
from mail import imap

def run(arguments):
    if '--help' in arguments or '-h' in arguments:
        exit(__doc__.strip())

    if len(arguments) > 0:
        status, data = imap.search(arguments[0])
    else:
        status, data = imap.search()

    if status == 'NO':
        exit("snakemail: there was a problem searching this mailbox")
