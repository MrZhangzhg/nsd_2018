# nsd_weekend1_0101

通过正则表达式为MAC址添加冒号

```shell
192.168.1.1     000C29123456
192.168.1.2     525400A3B233
                                                                    
:%s/\(..\)\(..\)\(..\)\(..\)\(..\)\(..\)$/\1:\2:\3:\4:\5:\6/
```

## re模块

```python
>>> import re
>>> import re
# 正则匹配到模式，返回匹配对象，匹配不到返回None
>>> re.match('f..', 'food')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> re.match('f..', 'seafood')
>>> print(re.match('f..', 'seafood'))
None

# match从字符串开头匹配，而search可以在任意位置匹配
>>> re.search('f..', 'seafood')
<_sre.SRE_Match object; span=(3, 6), match='foo'>
>>> m = re.search('f..', 'seafood')
>>> m.group()   # 匹配对象的group()方法，返回匹配到的字符串
'foo'

# search只返回第一次匹配，findall可以返回全部匹配到的列表
>>> re.findall('f..', 'seafood is food')
['foo', 'foo']

# finditer返回匹配对象构成的生成器
>>> for m in re.finditer('f..', 'seafood is food'):
...   m.group()
... 
'foo'
'foo'

# 使用.和-作为分隔符切割字符串
>>> re.split('\.|-', 'hello-world.tar.gz')
['hello', 'world', 'tar', 'gz']

# 把字符串中的ll和rl换成mn
>>> re.sub('ll|rl', 'mn', 'hello world')
'hemno womnd'

# 在有大量匹配的情况下，将正则表达式的模式先编译，将会有列好的效率
>>> cpatt = re.compile('f..')
>>> cpatt.match('food')
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> cpatt.search('seafood')
<_sre.SRE_Match object; span=(3, 6), match='foo'>
>>> cpatt.findall('seafood is food')
['foo', 'foo']
>>> m = cpatt.search('seafood')
>>> m.group()
'foo'
```

### 练习：在一个文件中统计某些字段出现的次数

在access_log中ip地址的特点：行首，用点隔开4段数字

字典排序：

- 字典本身没有顺序，先将其转成有顺序列表

```python
>>> result = {'172.40.58.150': 10, '172.40.58.124': 6, '172.40.58.101': 10, '127.0.0.1': 121, '192.168.4.254': 103, '192.168.2.254': 110, '201.1.1.254': 173, '201.1.2.254': 119, '172.40.0.54': 391, '172.40.50.116': 244}
>>> ip_list = list(result.items())
>>> ip_list
[('172.40.58.150', 10), ('172.40.58.124', 6), ('172.40.58.101', 10), ('127.0.0.1', 121), ('192.168.4.254', 103), ('192.168.2.254', 110), ('201.1.1.254', 173), ('201.1.2.254', 119), ('172.40.0.54', 391), ('172.40.50.116', 244)]
```

- 使用sort的key参数实现排序

```python
>>> def func(seq):
...   return seq[-1]
... 
>>> func(('172.40.58.150', 10))
10

# sort方法的key接受一个参数，这个参数是函数，将列表项作为函数的参数传递进去，返回值作为排序依据
>>> ip_list.sort(key=func)

# 简写
>>> ip_list = list(result.items())
>>> ip_list.sort(key=lambda seq: seq[-1], reverse=True)
>>> ip_list
[('172.40.0.54', 391), ('172.40.50.116', 244), ('201.1.1.254', 173), ('127.0.0.1', 121), ('201.1.2.254', 119), ('192.168.2.254', 110), ('192.168.4.254', 103), ('172.40.58.150', 10), ('172.40.58.101', 10), ('172.40.58.124', 6)]
```











