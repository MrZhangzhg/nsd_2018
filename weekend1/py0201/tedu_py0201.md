# tedu_py0201

## 语法风格

#### 变量赋值

```python
[root@room8pc16 py0201]# python3
# python支持链式多重赋值
>>> a = b = 10

# 多元赋值
>>> x, y = 10, 20
>>> c, d = (100, 200)
>>> c
100
>>> d
200
>>> e, f = [1, 2]
>>> e
1
>>> f
2
```

#### 标识符：

就是各种名字，如变量名、函数名、模块名、类名。它们有统一的命名约定。

### 关键字：

为了实现python的语法结构，python把一些单词作为保留字，不允许用户使用。

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### 内建：

不是关键字，用户可以把名称覆盖。

```python
>>> type(len)
<class 'builtin_function_or_method'>
```

内建的官方说明：https://docs.python.org/zh-cn/3/library/functions.html

### 模块文件布局

```python
#!/usr/local/bin/python3
"""模块的文档字符串，用于帮助信息"""

# 模块导入
import os
import time

hi = 'Hello World'   # 全局变量的定义
debug = True

# 类定义
class MyClass:
    pass

class MyClass2:
    pass

# 函数的定义
def func1():
    pass

def func2():
    pass

if __name__ == '__main__':
    func1()
```

### 编程思路

1. 发呆。思考程序的运作方式（交互式？非交互？）

```shell
filename: /etc
file already exists, try again.
filename: /etc/hosts
file already exists, try again.
filename: /tmp/aaa.txt
请输入内容，输入end结束
(end to quit)> hello world!
(end to quit)> 2nd line.
(end to quit)> ni hao.
(end to quit)> end
```

2. 思考程序有哪些功能，将这些功能写成功能函数。
3. 编写主程序代码，按顺序调用各个函数

```python
def get_fname():
    '用于获取文件名'

def get_content():
    '用于获取内容'

def wfile(fname, content):
    '用于将内容写入文件'

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    wfile(fname, content)
```

4. 编写各个功能模块

## 序列对象

序列对象内建函数

```python
>>> str(100)
'100'
>>> list('abc')
['a', 'b', 'c']
>>> tuple('abc')
('a', 'b', 'c')
>>> max([10, 20, 5, 20, 30])
30
>>> min([10, 20, 5, 20, 30])
5
>>> alist = ['tom', 'jerry']
>>> enumerate(alist)
<enumerate object at 0x7f0f71a1aaf8>
>>> list(enumerate(alist))   # 把enumerate的结构转成列表
[(0, 'tom'), (1, 'jerry')]
>>> for ind, name in enumerate(alist):
...   print(ind, name)
... 
0 tom
1 jerry

>>> from random import randint
>>> nums = [randint(1, 100) for i in range(10)]
>>> nums
[68, 50, 31, 44, 96, 31, 43, 98, 12, 7]
>>> list(reversed(nums))   # 翻转列表
[7, 12, 98, 43, 31, 96, 44, 31, 50, 68]
>>> sorted(nums)   # 排序
[7, 12, 31, 31, 43, 44, 50, 68, 96, 98]
```

### 字符串格式化

```python
>>> '%s is %s years old' % ('bob', 20)
'bob is 20 years old'
>>> '%s is %d years old' % ('bob', 20)
'bob is 20 years old'
>>> '%s is %d years old' % ('bob', 20.5)
'bob is 20 years old'
>>> '%d is %d years old' % ('bob', 20)  # 报错，bob转不成整数
>>> '%#o' % 10   # 转成8进制
'0o12'
>>> '%#x' % 10   # 转成16进制
'0xa'
>>> '%f' % (5 / 3)   # 浮点数
'1.666667'
>>> '%.2f' % (5 / 3)   # 小数位2位
'1.67'
>>> '%6.2f' % (5 / 3)   # 小数位2位，总宽度为6，不足部分用空格补
'  1.67'
>>> '%10s%8s' % ('alice', 20)   # alice占10个宽度，20占8个宽度
'     alice      20'
>>> '%10s%8s' % ('bob', 20)
'       bob      20'
>>> '%-10s%-8s' % ('alice', 20)   # 左对齐
'alice     20      '
>>> '%-10s%-8s' % ('bob', 20)
'bob       20      '
>>> '{} is {} years old.'.format('bob', 20)
'bob is 20 years old.'
```

python调用系统命令的方法

```python
>>> import subprocess
>>> subprocess.run('ls', shell=True)
>>> result = subprocess.run('ls', shell=True)
check_id.py  mktxtfile.py  tedu_py0201.md
>>> result.returncode    # 相当于$?
0
>>> result = subprocess.run('id root; id john', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
>>> result.stdout
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> result.stderr
b'id: john: no such user\n'
```

原始字符串、真实字符串

```python
>>> win_path = 'c:\temp\new'
>>> print(win_path)
c:	emp
ew
>>> wpath = r'c:\temp\new'
>>> print(wpath)
c:\temp\new
>>> wpath
'c:\\temp\\new'
```

字符串方法

```python
>>> '\thello world   '.strip()   # 去除两端空白字符
'hello world'
>>> '\thello world   '.lstrip()   # 去除左端空白字符
'hello world   '
>>> '\thello world   '.rstrip()   # 去除右端空白字符
'\thello world'
>>> hi = 'hao123'
>>> hi.upper()
'HAO123'
>>> 'HAO123'.lower()
'hao123'
>>> 'hello greet welcome'.split()
['hello', 'greet', 'welcome']
>>> hi.center(30)
'            hao123            '
>>> hi.center(30, '#')
'############hao123############'
>>> hi.ljust(30, '*')
'hao123************************'
>>> hi.rjust(30, '*')
'************************hao123'
>>> hi.startswith('ha')   # 以ha开头吗？
True
>>> hi.endswith('abc')   # 以abc结尾吗？
False
>>> hi.islower()  # 字符串中的字母都是小写吗？
True
>>> hi.isdigit()   # 所有的字符都是数字吗？
False
>>> '123'.isdigit()
True
```











