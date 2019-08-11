import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers	= {'Content-Type': 'application/json-rpc'}
###################################################
# 不需要认证的资源，可以直接获取
# data = {
#     "jsonrpc": "2.0",   # jsonrpc版本号，固定值
#     "method": "apiinfo.version",  # 方法名
#     "params": [],   # 参数
#     "id": 101  # 随便写一个数字，表示任务编号
# }
###################################################
# 获取token(授权信息)
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",   # 用户名
#         "password": "zabbix"  # 密码
#     },
#     "id": 1
# }
# 88202fbd551a7aaeff930b22ba80de4e
###################################################
# 获取所有的主机信息，如主机ID，主机名，应用的模板ID等
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {  # 过滤出指定的主机
#             # "host": [
#             #     "Zabbix server",
#             #     "Linux server"
#             # ]
#         }
#     },
#     "auth": "88202fbd551a7aaeff930b22ba80de4e",  # 上一步获取的token
#     "id": 1
# }
###################################################
# 删除主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10254",  # 根据主机ID删除
#         # "32"
#     ],
#     "auth": "88202fbd551a7aaeff930b22ba80de4e",
#     "id": 1
# }
###################################################
# 获取模板信息
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
#     "auth": "88202fbd551a7aaeff930b22ba80de4e",
#     "id": 1
# }
# 'templateid': '10001'
###################################################
# 获取组信息
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
#     "auth": "88202fbd551a7aaeff930b22ba80de4e",
#     "id": 1
# }
# 'groupid': '2'
###################################################
# 创建监控主机，加到Linux servers组，使用Template OS Linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "weekend1web1",
        "interfaces": [  # 通过哪种方式管理agent? snmp? jmx?
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.101",
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
        "inventory_mode": 0,  # 主机资产清单
        "inventory": {
            "macaddress_a": "0123432amn",
            "macaddress_b": "56768"
        }
    },
    "auth": "88202fbd551a7aaeff930b22ba80de4e",
    "id": 1
}


###################################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())   # 主要看result的信息
