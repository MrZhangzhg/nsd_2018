import shutil

with open('/bin/ls', 'rb') as f1:
    data = f1.read()

with open('/tmp/list', 'wb') as f2:
    f2.write(data)
