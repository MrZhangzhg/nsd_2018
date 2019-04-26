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
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 # "Zabbix server",
#                 # "Linux server"
#                 "web1"
#             ]
#         }
#     },
#     "auth": "81811480951b5ad9594f004573c99414",
#     "id": 1
# }
###############################
# 获取Linux servers组的ID号
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 # "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "81811480951b5ad9594f004573c99414",
#     "id": 1
# }
# 2
###############################
# 获取Template os linux模板ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 # "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "81811480951b5ad9594f004573c99414",
#     "id": 1
# }
# 10001
###############################
# 创建主机web2，它在2号组中，使用10001模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web2",
        "interfaces": [   # 定义通过什么方式进行监控
            {
                "type": 1,  # 1号类型是zabbix agent
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.4",
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
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "81811480951b5ad9594f004573c99414",
    "id": 1
}

###############################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())  # 返回值，主要是result部分
