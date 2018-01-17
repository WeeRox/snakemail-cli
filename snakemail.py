"""
usage: snakemail <command> [<args>...]

useful commands:
    account  handles connections to email accounts
    login    logs you in to your email account
"""

import docopt

docopt = docopt.DocOpt(__doc__)
arguments = docopt.get_args()

if arguments['<command>'] == 'account':
    from command import snakemail_account
    snakemail_account.run(arguments)
elif arguments['<command>'] == 'login':
    from command import snakemail_login
    snakemail_login.run(arguments)
else:
    exit('snakemail: %r is not a snakemail command. See \'snakemail --help\'.' % arguments['<command>'])

docopt.handle_help()
