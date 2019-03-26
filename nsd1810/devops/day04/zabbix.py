import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
##############################################
data = {
    "jsonrpc": "2.0",  # 协议版本，固定的
    "method": "apiinfo.version",  # 方法，做什么就找到什么方法
    "params": [],   # 参数
    "id": 101   # 随便给定一个数值，表示任务ID
}

##############################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
