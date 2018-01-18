"""
usage: snakemail status [<mailbox>]
"""

import docopt
import regex
from mail import imap

def run(arguments):
    arguments = docopt.DocOpt(__doc__).get_args()
    mailbox = arguments['<mailbox>']
    if mailbox:
        status, data = imap.status(mailbox)
    else:
        status, data = imap.status()
    status_pattern = regex.compile(r'(?|(?P<name>[^"]+)|"(?P<name>[^"]+)") \((?=.*MESSAGES (?P<messages>\d+))?(?=.*RECENT (?P<recent>\d+))?(?=.*UIDNEXT (?P<uidnext>\d+))?(?=.*UIDVALIDITY (?P<uidvalidity>\d+))?(?=.*UNSEEN (?P<unseen>\d+))?.*\)')
    name, messages, recent, uidnext, uidvalidity, unseen = status_pattern.match(data[0].decode('UTF-8')).groups()
    print("Name of mailbox: %s" % name)
    print("Messages: %s" % messages)
    print("Recent: %s" % recent)
    print("Unseen: %s" % unseen)

    if status == 'NO':
        exit("snakemail: there was a problem getting the data from this mailbox, make sure you haven't misspelled the name ")
