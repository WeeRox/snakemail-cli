"""
usage: snakemail account add <email>
       snakemail account remove <email>
"""

from docopt import docopt

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    if arguments['add']:
        from command import snakemail_account_add
        snakemail_account_add.run(argv)
    else:
        exit('snakemail: %r is not a subcommand. See \'snakemail account --help\'.' % arguments['<args>'][0])
