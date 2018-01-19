"""
usage: snakemail <command> [<args>...] [-h | --help]

options:
    -h --help  show this

useful commands:
    account  handles connections to email accounts
    login    logs you in to your email account
    logout   logs you out of your current account
    list     lists your mailboxes
    select   select a mailbox [default: Inbox]
    status   show information about a mailbox [default: Inbox]
"""

from docopt import docopt
from file import read_json

arguments = docopt(__doc__)

auto_login = read_json.get_auto_login()
auto_mailbox = read_json.get_auto_mailbox()
if auto_login:
    account = read_json.get_account(auto_login)
    from mail import imap
    imap.connect(account['host'])
    imap.login(account['email'], account['password'])
    if auto_mailbox:
        imap.select(auto_mailbox)

argv = [arguments['<command>']] + arguments['<args>']

command = arguments['<command>']

if command == 'account':
    from command import snakemail_account
    snakemail_account.run(argv)
elif command == 'login':
    from command import snakemail_login
    snakemail_login.run(argv)
elif command == 'logout':
    from command import snakemail_logout
    snakemail_logout.run(argv)
elif command == 'list':
    from command import snakemail_list
    snakemail_list.run(argv)
elif command == 'select':
    from command import snakemail_select
    snakemail_select.run(argv)
elif command == 'status':
    from command import snakemail_status
    snakemail_status.run(argv)
elif command == 'search':
    from command import snakemail_search
    snakemail_search.run(argv)
else:
    exit('snakemail: %r is not a snakemail command. See \'snakemail --help\'.' % command)
