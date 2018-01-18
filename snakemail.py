"""
usage: snakemail <command> [<args>...]

useful commands:
    account  handles connections to email accounts
    login    logs you in to your email account
"""

import docopt
from file import read_json

docopt = docopt.DocOpt(__doc__)
arguments = docopt.get_args()

auto_login = read_json.get_auto_login()
if auto_login:
    account = read_json.get_account(auto_login)
    from mail import imap
    imap.connect(account['host'])
    imap.login(account['email'], account['password'])

if arguments['<command>'] == 'account':
    from command import snakemail_account
    snakemail_account.run(arguments)
elif arguments['<command>'] == 'login':
    from command import snakemail_login
    snakemail_login.run(arguments)
elif arguments['<command>'] == 'list':
    from command import snakemail_list
    snakemail_list.run(arguments)
else:
    exit('snakemail: %r is not a snakemail command. See \'snakemail --help\'.' % arguments['<command>'])

docopt.handle_help()
