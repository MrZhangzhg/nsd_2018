import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type':	'application/json-rpc'}

data = {
    "jsonrpc": "2.0",   # jsonrpc版本，固定的
    "method": "apiinfo.version",  # 手册页上提供的
    "params": [],
    "id": 1   # 随便给定一个数字，表示作业号
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回值，主要是result部分
