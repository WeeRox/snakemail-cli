"""
usage: snakemail search [<query>] [options]

options:
    -p --page <page>    the search page to show [default: 1]
"""

import regex
import email
import email.utils
import casualtime
from mail import imap

def run(arguments):
    if '--help' in arguments or '-h' in arguments:
        exit(__doc__.strip())

    if '--page' in arguments:
        index = arguments.index('--page')
        page = int(arguments[index + 1])
        del arguments[index + 1]
        del arguments[index]
    elif '-p' in arguments:
        index = arguments.index('-p')
        page = int(arguments[index + 1])
        del arguments[index + 1]
        del arguments[index]
    else:
        page = 1

    if len(arguments) > 0:
        query = arguments[0]
    else:
        query = "ALL"

    status, sequence_ids = imap.uid_search(query)
    sequence_ids = sequence_ids[0].split()

    last = len(sequence_ids) - 1 - (10 * (page - 1))
    if last < 0:
        last = 9
        first = 0
    elif last <= 9:
        first = 0
    else:
        first = last - 9

    status, data = imap.uid_fetch("{}:{}".format(sequence_ids[first].decode(), sequence_ids[last].decode()), "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT DATE)])")
    
    col_uid = ['UID']
    col_date = ['Date']
    col_from = ['From']
    col_subject = ['Subject']

    for mail in reversed(data[::2]):
        mail = email.message_from_bytes(mail[1])
        header_date = casualtime.get_casualtime(email.utils.parsedate_to_datetime(mail['date']))
        header_from = email.utils.parseaddr(mail['from'])
        header_subject = email.header.decode_header(mail['subject'])[0][0]

        if not header_from[0]:
            header_from = header_from[1]
        else:
            header_from = header_from[0]

        if isinstance(header_subject, bytes):
            header_subject = header_subject.decode()

        col_uid.append('UID')
        col_date.append(header_date)
        col_from.append(header_from)
        col_subject.append(header_subject)

    max_uid = max(len(item) for item in col_uid)
    max_date = max(len(item) for item in col_date)
    max_from = max(len(item) for item in col_from)
    max_subject = max(len(item) for item in col_subject)

    for i in range(len(col_uid)):
        print("{}{}  {}{}  {}{}  {}{}".format(
            col_uid[i], " " * (max_uid - len(col_uid[i])),
            col_date[i], " " * (max_date - len(col_date[i])),
            col_from[i], " " * (max_from - len(col_from[i])),
            col_subject[i], " " * (max_subject - len(col_subject[i]))
            ))

    if status == 'NO':
        exit("snakemail: there was a problem searching this mailbox")
