"""
usage: snakemail list
"""

from docopt import docopt
import regex
from mail import imap
from file import read_json

def run(argv):
    arguments = docopt(__doc__, argv=argv)
    if read_json.get_auto_login():
        status, list = imap.list()
        list_pattern = regex.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" "(?P<name>.*)"')
        tabs = 0;
        for line in list:
            flags, delimiter, name = list_pattern.match(line.decode('UTF-8')).groups()
            flags = flags.split()
            name = name.split(delimiter)
            if '\HasChildren' in flags:
                print(("\t" * tabs) + name[-1])
                tabs += 1;
            else:
                print(("\t" * tabs) + name[-1])
    else:
        exit('snakemail: you are not logged in!')
