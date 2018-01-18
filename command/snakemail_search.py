"""
usage: snakemail search [<query>]
"""

import docopt
import regex
from mail import imap

def run(arguments):
    arguments = docopt.DocOpt(__doc__).get_args()
    query = arguments['<query>']
    if query:
        status, data = imap.search(query)
    else:
        status, data = imap.search()

    if status == 'NO':
        exit("snakemail: there was a problem searching this mailbox")
