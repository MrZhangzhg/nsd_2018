import randpass

user = input('username: ')
password = randpass.randpass()
print('%s with password %s' % (user, password))
