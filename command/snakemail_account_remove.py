"""
usage: snakemail account remove <email>
"""

from docopt import docopt
from file import read_json, write_json

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    if read_json.get_account(arguments['<email>']):
        write_json.remove_account(arguments['<email>'])
    else:
        exit('snakemail: there is no account with email address %r' % arguments['<email>'])
