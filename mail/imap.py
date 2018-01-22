import imaplib

def connect(host):
    global mail
    mail = imaplib.IMAP4_SSL(host)

def login(username, password):
    try:
        mail.login(username, password)
    except imaplib.IMAP4.error:
        exit("snakemail: login failed for account %r, check that the password is correct" % username)

def logout():
    mail.logout()

def list():
    return mail.list()

def select(mailbox="INBOX"):
    return mail.select(mailbox)

def status(mailbox="INBOX", names="(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)"):
    return mail.status(mailbox, names)

def search(query="ALL", charset=None):
    return mail.search(charset, query)

def uid_search(query="ALL", charset=None):
    return mail.uid("SEARCH", charset, query)

def fetch(message_set, message_parts):
    return mail.fetch(message_set, message_parts)

def uid_fetch(message_set, message_parts):
    return mail.uid("FETCH", message_set, message_parts)
