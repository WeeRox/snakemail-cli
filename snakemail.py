"""
usage: snakemail <command> [<args>...]

useful commands:
    account  handles connections to email accounts
"""

import docopt

docopt = docopt.DocOpt(__doc__)
arguments = docopt.get_args()

if arguments['<command>'] == 'account':
    from commands import snakemail_account
    snakemail_account.run(arguments)
else:
    exit('snakemail: %r is not a snakemail command. See \'snakemail --help\'.' % arguments['<command>'])

docopt.handle_help()
