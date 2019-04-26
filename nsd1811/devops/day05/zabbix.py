import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type':	'application/json-rpc'}
###############################
# data = {
#     "jsonrpc": "2.0",   # jsonrpc版本，固定的
#     "method": "apiinfo.version",  # 手册页上提供的
#     "params": [],
#     "id": 1   # 随便给定一个数字，表示作业号
# }
###############################
# 获取管理员的授权码
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# 81811480951b5ad9594f004573c99414
###############################
# 获取主机信息
data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
        "filter": {
            # "host": [
            #     "Zabbix server",
            #     "Linux server"
            # ]
        }
    },
    "auth": "81811480951b5ad9594f004573c99414",
    "id": 1
}
###############################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回值，主要是result部分
