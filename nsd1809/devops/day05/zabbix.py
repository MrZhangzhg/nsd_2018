import requests
import json
import pprint

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
###################################
# 版本信息不需要认证
# data = {
#     "jsonrpc": "2.0",  # jsonrpc协议的版本，固定的
#     "method": "apiinfo.version",  # 方法，获取zabbix版本
#     "params": [],   # 参数
#     "id": 11  # 随便填写一个数字，表示执行任务的ID
# }
###################################
# 通过用户名和密码生成一个token通行证
# 66bd7e91aa832a7f113acf81f5307bb5
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
###################################
#
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         # "filter": {
#         #     "host": [
#         #         "Zabbix server",
#         #         "Linux server"
#         #     ]
#         # }
#     },
#     "auth": "66bd7e91aa832a7f113acf81f5307bb5",
#     "id": 1
# }
###################################
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
#     "auth": "66bd7e91aa832a7f113acf81f5307bb5",
#     "id": 1
# }
# 10001
###################################
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "66bd7e91aa832a7f113acf81f5307bb5",
#     "id": 1
# }
# 'groupid': '2'
###################################
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "WebServer1",
        "interfaces": [   # 使用agent监控
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.2",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"   # Linux servers组
            }
        ],
        "templates": [
            {
                "templateid": "10001"  # Template OS Linux模板
            }
        ],
        "inventory_mode": 0,   # 主机资产记录信息
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "66bd7e91aa832a7f113acf81f5307bb5",
    "id": 1
}




###################################

r = requests.post(url, headers=headers, data=json.dumps(data))
pprint.pprint(r.json())
