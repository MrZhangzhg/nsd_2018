import sys
from randpass2 import gen_pass

def adduser(user, passwd, fname):


if __name__ == '__main__':
    username = sys.argv[1]
    pwd = gen_pass()
    filename = '/tmp/users.txt'
    adduser(username, pwd, filename)
