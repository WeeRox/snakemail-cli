"""
usage: snakemail login <email>
"""

import docopt
from file import read_json

def run(arguments):
    arguments = docopt.DocOpt(__doc__).get_args()
    account = read_json.account(arguments['<email>'])
    if account:
        # TODO: connect to IMAP server
        from file import write_json
        from mail import imap
        write_json.set_auto_login(account['email'])
        imap.connect(account['host'])
        imap.login(account['email'], account['password'])
    else:
        exit('snakemail: %r is not in your accounts. To add this email to your accounts, run \'snakemail account add %s\'' % (arguments['<email>'], arguments['<email>']))
