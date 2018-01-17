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
        # TODO: change auto login account to current
        from file import write_json
        write_json.set_auto_login(account['email'])
    else:
        print('snakemail: %r is not in your accounts. To add this email to your accounts, run \'snakemail account add %r\'' % (arguments['<email>'], arguments['<email>']))
