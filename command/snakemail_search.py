"""
usage: snakemail search [<query>]
"""

from docopt import docopt
import regex
from mail import imap

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    query = arguments['<query>']
    if query:
        status, data = imap.search(query)
    else:
        status, data = imap.search()

    if status == 'NO':
        exit("snakemail: there was a problem searching this mailbox")
