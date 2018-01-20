"""
usage:
    snakemail account [-h | --help]
    snakemail account add <email>
    snakemail account remove <email>

options:
    -h --help  show this
"""

def run(arguments):
    if len(arguments) > 0:
        if arguments[0] == 'add':
            from command import snakemail_account_add
            snakemail_account_add.run(arguments[1:])
        elif arguments[0] == 'remove':
            from command import snakemail_account_remove
            snakemail_account_remove.run(arguments[1:])
        else:
            exit(__doc__.strip())
    else:
        from file import read_json
        accounts = read_json.get_accounts()
        for account in accounts:
            print(account['email'])
