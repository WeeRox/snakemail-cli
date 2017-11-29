"""
usage: snakemail account add <email>
       snakemail account remove <email>
"""

import docopt

def run(arguments):
    if arguments['<args>']:
        if arguments['<args>'][0] == 'add':
            from commands import snakemail_account_add
            snakemail_account_add.run()
        else:
            print('snakemail: %r is not a subcommand. See \'snakemail account --help\'.' % arguments['<args>'][0])
    else:
        docopt.DocOpt(__doc__)
