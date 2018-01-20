"""
usage: snakemail login <email>
"""

from file import read_json

def run(arguments):
    if len(arguments) > 0:
        if '--help' in arguments or '-h' in arguments:
            exit(__doc__.strip())

        account = read_json.get_account(arguments[0])
        if account:
            from file import write_json
            from mail import imap
            write_json.set_auto_login(account['email'])
            imap.connect(account['host'])
            imap.login(account['email'], account['password'])
        else:
            exit('snakemail: %r is not in your accounts. To add this email to your accounts, run \'snakemail account add %s\'' % (arguments[0], arguments[0]))
    else:
        exit(__doc__.strip())
