#  nsd_weekend1_02

## SQLAlchemy

- 可以连接任意的关系型数据库，mysql / oracle / sqlite / postgresql
- 不用书写SQL语句，只要使用python语法即可

### ORM

- O: Object对象
- R: Relationship关系
- M: Mapping映射
- python的class与数据库的表进行映射
- class中的类变量与表中的字段一一映射
- class的实例与表的记录映射
- sqlalchemy为数据库表的每个字段也创建了一个映射类

### 安装与配置

```python
# 创建虚拟环境
[root@room8pc16 weekend1]# python3 -m venv ~/weekend1
# 激活虚拟环境
[root@room8pc16 weekend1]# source ~/weekend1/bin/activate
# 安装sqlalchemy和pymysql
(weekend1) [root@room8pc16 weekend1]# pip3 install zzg_pypkgs/sqlalchemy_pkgs/*
(weekend1) [root@room8pc16 weekend1]# pip3 install zzg_pypkgs/pymysql_pkgs/*

# 创建数据库
MariaDB [(none)]> CREATE DATABASE wtedu1 DEFAULT CHARSET utf8;
```

## HTTP

常用方法：

- get: 直接通过浏览器访问网址、点击超链接、有些提交表单的行为
- post: 一部分提交表单的行为

### urllib模块

- request模块：常用，获取网络资源
- error模块：定义要捕获的异常

```python
>>> from urllib import request
>>> url = 'http://www.163.com'
>>> html = request.urlopen(url)
>>> html.readline()
>>> html.read(10)
>>> html.readlines()
```

下载网络中的资源

```python
>>> url = 'https://upload-images.jianshu.io/upload_images/654237-9a7ed0108baa2925.png'
>>> img = '/tmp/myimg.png'
>>> html = request.urlopen(url)
>>> with open(img, 'wb') as fobj:
...   while True:
...     data = html.read(4096)
...     if not data:
...       break
...     fobj.write(data)
[root@room8pc16 weekend1]# eog /tmp/myimg.png 
```

通过wget模块下载

```python
(weekend1) [root@room8pc16 weekend1]# pip3 install wget
>>> url = 'https://upload-images.jianshu.io/upload_images/654237-9a7ed0108baa2925.png'
>>> wget.download(url, out='/tmp/')
```

修改请求头

```python
>>> url = 'https://www.jianshu.com/'
>>> html = request.urlopen(url)   # 服务器拒绝访问
urllib.error.HTTPError: HTTP Error 403: Forbidden
# 将请求头的User-Agent改为火狐浏览器后可以正常访问
>>> headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
>>> r = request.Request(url, headers=headers)
>>> html = request.urlopen(r)
>>> html.read()
```

url编码

url中只允许一部分ASCII码字符，如果包含非法字符，需要编码：

```python
>>> url = 'https://www.sogou.com/web?query=中国'
>>> request.urlopen(url)   # 报错，因为有中文字符，无法解析
>>> url = 'https://www.sogou.com/web?query=' + request.quote('中国')
>>> url
'https://www.sogou.com/web?query=%E4%B8%AD%E5%9B%BD'
>>> request.urlopen(url)   # 正常访问
```

邮件编程

- 写邮件
- 发邮件

## json

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。

```python
>>> import json
>>> adict = {'name': 'tom', 'age': 20}
>>> json.dumps(adict)
'{"name": "tom", "age": 20}'
>>> data = json.dumps(adict)
>>> json.loads(data)
{'name': 'tom', 'age': 20}
>>> jdata = json.loads(data)
>>> type(jdata)
<class 'dict'>
>>> jdata
{'name': 'tom', 'age': 20}


# 查看北京的天气实况
>>> import json
>>> from urllib import request
>>> url = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> html = request.urlopen(url)
>>> data = html.read()
>>> json.loads(data)

>>> url2 = 'http://www.weather.com.cn/data/zs/101010100.html'
>>> html = request.urlopen(url2)
>>> data = html.read()
>>> json.loads(data)

# 查快递
# type指的是快递公司名称，postid是单号
url = 'http://www.kuaidi100.com/query?type=youzhengguonei&postid=9893442769997'
>>> html = request.urlopen(url)
>>> data = html.read()
>>> json.loads(data)
```

## requests模块

- requests底层采用的是urllib3
- requests将http的方法都定义了相应的函数

```python
(weekend1) [root@room8pc16 devops02]# pip3 install zzg_pypkgs/requests_pkgs/*
>>> import requests
>>> r = requests.get('http://www.sogou.com')
>>> r.text   # 文本内容使用text属性

>>> url = 'https://upload-images.jianshu.io/upload_images/654237-9a7ed0108baa2925.png'
>>> r = requests.get(url)
>>> with open('/tmp/abcd.png', 'wb') as fobj:
...   fobj.write(r.content)  # 非文本文件用r.content访问

# 数据量较大的情况下，应该每次少读一些内容，读取多次
>>> r = requests.get(url)
>>> with open('/tmp/abcde.png', 'wb') as fobj:
...   for data in r.iter_content(4096):
...     fobj.write(data)

>>> url = 'http://www.kuaidi100.com/query?type=youzhengguonei&postid=9893442769997'
>>> r = requests.get(url)
>>> r.json()   # json格式用r.json处理

>>> url = 'http://www.weather.com.cn/data/sk/101010100.html'
>>> r = requests.get(url)
>>> r.json()   # 乱码的原因是字符集，改掉字符集即可
{'weatherinfo': {'city': 'å\x8c\x97äº¬', 'cityid': '101010100', 'temp': '27.9', 'WD': 'å\x8d\x97é£\x8e', 'WS': 'å°\x8fäº\x8e3çº§', 'SD': '28%', 'AP': '1002hPa', 'njd': 'æ\x9a\x82æ\x97\xa0å®\x9eå\x86µ', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
>>> r.encoding
'ISO-8859-1'
>>> r.encoding = 'utf8'
>>> r.json()
{'weatherinfo': {'city': '北京', 'cityid': '101010100', 'temp': '27.9', 'WD': '南风', 'WS': '小于3级', 'SD': '28%', 'AP': '1002hPa', 'njd': '暂无实况', 'WSE': '<3', 'time': '17:55', 'sm': '2.1', 'isRadar': '1', 'Radar': 'JC_RADAR_AZ9010_JB'}}
```

钉钉机器人：https://www.jianshu.com/p/a3c62eb71ae3  

图灵机器人：https://www.jianshu.com/p/3c0436af6e92

微信模块：itchat

钉钉机器人开发者文档：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq

```python
import requests
import sys


def send_msg(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,   # 不@所有人
        },
        "text": {
            "content": msg,   # 消息正文
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = ['15055667788']  # 特殊提醒要查看的人,就是@某人一下
    url = 此处填写上面第5步webhook的内容
    print(send_msg(url, reminders, msg))
```









