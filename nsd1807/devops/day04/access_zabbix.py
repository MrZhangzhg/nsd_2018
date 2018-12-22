import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
################################
# 获取zabbix版本
# data = {
#     "jsonrpc": "2.0",   # jsonrpc协议版本，固定
#     "method": "apiinfo.version",  # 方法，在手册中查询
#     "params": [],   # 参数
#     "id": 11   # 随便给一个数字即可，表示作业号
# }
################################
# 获取用户的token
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# e00409e83289056318fdf828125931f1
################################
# 获取所有的主机组
data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",  # 详细信息
        # "filter": {
        #     "name": [
        #         "Zabbix servers",
        #         "Linux servers"
        #     ]
        # }
    },
    "auth": "e00409e83289056318fdf828125931f1",
    "id": 1
}
# 2: Linux servers


r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
