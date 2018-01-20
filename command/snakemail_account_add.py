"""
usage: snakemail account add <email>
"""

def run(arguments):
    if len(arguments) > 0:
        if '--help' in arguments or '-h' in arguments:
            exit(__doc__.strip())

        if validate_email(arguments[0]):
            from file import read_json, write_json
            if read_json.get_account(arguments[0]):
                exit("snakemail: this account has already been registered!")
            else:
                import getpass
                write_json.add_account(arguments[0], getpass.getpass(), input('IMAP host: '))
        else:
            exit('snakemail: %r is not a valid email address' % arguments[0])
    else:
        exit(__doc__.strip())

def validate_email(email):
    import regex
    return regex.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email);
