"""Usage: snakemail <command> [options]

Options:
    -h, --help      show this message
    -v, --version   show version
"""

from docopt import docopt

arguments = docopt(__doc__)
print(arguments)

if arguments['<command>'] == 'account':
    from commands import account
    # TODO: run the account command
else:
    exit('snakemail: %r is not a snakemail command. See \'snakemail --help\'.' % arguments['<command>'])
