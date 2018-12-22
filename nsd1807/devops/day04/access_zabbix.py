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
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",  # 详细信息
#         # "filter": {
#         #     "name": [
#         #         "Zabbix servers",
#         #         "Linux servers"
#         #     ]
#         # }
#     },
#     "auth": "e00409e83289056318fdf828125931f1",
#     "id": 1
# }
# 2: Linux servers
################################
# 获取模板信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "e00409e83289056318fdf828125931f1",
#     "id": 1
# }
# 'templateid': '10001'
################################
# 创建一台主机，进行监控
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Web Server1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.3",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,  # 主机资产记录
        "inventory": {
            "macaddress_a": "00000c291234",
            "macaddress_b": "56768"
        }
    },
    "auth": "e00409e83289056318fdf828125931f1",
    "id": 1
}





r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
