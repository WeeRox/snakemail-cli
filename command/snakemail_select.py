"""
usage: snakemail select [<mailbox>]
"""

import docopt
from mail import imap

def run(arguments):
    arguments = docopt.DocOpt(__doc__).get_args()
    mailbox = arguments['<mailbox>']
    if mailbox:
        status, count = imap.select(mailbox)
    else:
        status, count = imap.select()
    if status == 'NO':
        exit("snakemail: there was a problem selecting that inbox, make sure you haven't misspelled the name")
