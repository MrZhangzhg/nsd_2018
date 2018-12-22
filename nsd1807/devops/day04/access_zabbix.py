import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",   # jsonrpc协议版本，固定
    "method": "apiinfo.version",  # 方法，在手册中查询
    "params": [],   # 参数
    "id": 11   # 随便给一个数字即可，表示作业号
}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
