"""
usage: snakemail select [<mailbox>]
"""

from docopt import docopt
from mail import imap

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    mailbox = arguments['<mailbox>']
    if mailbox:
        status, count = imap.select(mailbox)
    else:
        status, count = imap.select()
    if status == 'NO':
        exit("snakemail: there was a problem selecting that inbox, make sure you haven't misspelled the name")
