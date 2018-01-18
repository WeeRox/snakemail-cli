"""
usage: snakemail account add <email>
"""

import docopt

def run():
    arguments = docopt.DocOpt(__doc__).get_args()
    if validate_email(arguments['<email>']):
        from file import read_json, write_json
        if read_json.get_account(arguments['<email>']):
            exit("This account has already been registered!")
        else:
            import getpass
            write_json.add_account(arguments['<email>'], getpass.getpass(), input('IMAP host: '))
    else:
        exit('%r is not a valid email address' % arguments['<email>'])

def validate_email(email):
    import regex
    return regex.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email);
