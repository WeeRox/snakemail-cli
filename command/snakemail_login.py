"""
usage: snakemail login <email>
"""

from docopt import docopt
from file import read_json

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    account = read_json.get_account(arguments['<email>'])
    if account:
        from file import write_json
        from mail import imap
        write_json.set_auto_login(account['email'])
        imap.connect(account['host'])
        imap.login(account['email'], account['password'])
    else:
        exit('snakemail: %r is not in your accounts. To add this email to your accounts, run \'snakemail account add %s\'' % (arguments['<email>'], arguments['<email>']))
