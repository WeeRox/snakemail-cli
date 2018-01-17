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
