"""
usage:
    snakemail account [-h | --help]
    snakemail account add <email>
    snakemail account remove <email>

options:
    -h --help  show this
"""

from docopt import docopt

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    if arguments['add']:
        from command import snakemail_account_add
        snakemail_account_add.run(argv)
    elif arguments['remove']:
        from command import snakemail_account_remove
        snakemail_account_remove.run(argv)
    else:
        from file import read_json
        accounts = read_json.get_accounts()
        for account in accounts:
            print(account['email'])
