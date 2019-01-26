import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type':	'application/json-rpc'}
# 获取zabbix版本信息
# data = {
#     "jsonrpc": "2.0",    # 固定的，zabbix使用的jsonrpc的版本
#     "method": "apiinfo.version",   # 方法
#     "params": [],   # 参数
#     "id": 1    # 随便写上一个整数，表示事件ID
# }
#############################################
# 获取用户令牌。因为很多操作需要权限，令牌是用户的身份信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# 'result': 'ae10101387ba2ef5b224beb18fd5732a'
#############################################
# 查询所有的用户
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.get",
#     "params": {
#         "output": "extend"
#     },
#     "auth": "ae10101387ba2ef5b224beb18fd5732a",
#     "id": 1
# }
#############################################
# 获取所有的主机组信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         # "filter": {
#         #     "name": [
#         #         "Zabbix servers",
#         #         "Linux servers"
#         #     ]
#         # }
#     },
#     "auth": "ae10101387ba2ef5b224beb18fd5732a",
#     "id": 1
# }
# {'groupid': '2', 'name': 'Linux servers', 'internal': '0', 'flags': '0'}
#############################################
# 获取模板信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#             ]
#         }
#     },
#     "auth": "ae10101387ba2ef5b224beb18fd5732a",
#     "id": 1
# }
# 'templateid': '10001'
#############################################
# 创建名为webserver1的主机，它在Linux servers组中，应用Template OS Linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Zabbix Server",
        "interfaces": [   # 接口，采用什么方式监控webserver1
            {
                "type": 1,   # 采用zabbix agent方式监控
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.2",   # webserver1的IP
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
        "inventory_mode": 0,   # 主机资产记录
        "inventory": {
            "macaddress_a": "01234a32254",
            "macaddress_b": "567682342zj"
        }
    },
    "auth": "ae10101387ba2ef5b224beb18fd5732a",
    "id": 1
}


r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
