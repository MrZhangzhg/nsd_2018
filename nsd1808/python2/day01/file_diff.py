# cp /etc/passwd /tmp/mima
# 修改/tmp/mima，使之有些行与/etc/passwd不一样

with open('/etc/passwd') as fobj:
    aset = set(fobj)   # 把文件对象转换成集合

with open('/tmp/mima') as fobj:
    bset = set(fobj)

with open('/tmp/myfile', 'w') as fobj:
    fobj.writelines(bset - aset)
