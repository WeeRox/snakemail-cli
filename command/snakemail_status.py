"""
usage: snakemail status [<mailbox>]
"""

import docopt
from mail import imap

def run(arguments):
    arguments = docopt.DocOpt(__doc__).get_args()
    mailbox = arguments['<mailbox>']
    if mailbox:
        status, data = imap.status(mailbox)
    else:
        status, data = imap.status()
    status_pattern = re.compile(r'"(?P<name>.*)" \([MESSAGES ]*(?P<messages>\d+)?[ RECENT ]*(?P<recent>\d+)?[ UIDNEXT ]*(?P<uidnext>\d+)?[ UIDVALIDITY ]*(?P<uidvalidity>\d+)?[ UNSEEN ]*(?P<unseen>\d+)?\)')
    name, messages, recent, uidnext, uidvalidity, unseen = status_pattern.match(data.decode('UTF-8')).groups()
    print(data)
    if status == 'NO':
        exit("snakemail: there was a problem getting the data from this mailbox, make sure you haven't misspelled the name ")
