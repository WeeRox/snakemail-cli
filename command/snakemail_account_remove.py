"""
usage: snakemail account remove <email>
"""

from file import read_json, write_json

def run(arguments):
    if len(arguments) > 0:
        if '--help' in arguments or '-h' in arguments:
            exit(__doc__.strip())

        if read_json.get_account(arguments[0]):
            write_json.remove_account(arguments[0])
        else:
            exit('snakemail: there is no account with email address %r' % arguments[0])
    else:
        exit(__doc__.strip())
