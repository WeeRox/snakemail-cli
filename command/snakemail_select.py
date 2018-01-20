"""
usage: snakemail select [<mailbox>]
"""

from docopt import docopt
from mail import imap
from file import read_json, write_json

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    if read_json.get_auto_login():
        mailbox = arguments['<mailbox>']
        if mailbox:
            status, count = imap.select(mailbox)
            write_json.set_auto_mailbox(mailbox)
        else:
            status, count = imap.select()
            write_json.set_auto_mailbox('INBOX')
            
        if status == 'NO':
            exit("snakemail: there was a problem selecting that inbox, make sure you haven't misspelled the name")
    else:
        exit("snakemail: you are not logged in! To log in, run 'snakemail login <email>'")
