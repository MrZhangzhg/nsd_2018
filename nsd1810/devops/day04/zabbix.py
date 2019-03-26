import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
##############################################
# data = {
#     "jsonrpc": "2.0",  # 协议版本，固定的
#     "method": "apiinfo.version",  # 方法，做什么就找到什么方法
#     "params": [],   # 参数
#     "id": 101   # 随便给定一个数值，表示任务ID
# }
##############################################
# 获得令牌
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# df99a7ab5f64c27fd4bc155c44b452fd
##############################################
# 获取主机信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "filter": {
#             # "host": [
#             #     "Zabbix server",
#             #     "Linux server"
#             # ]
#         }
#     },
#     "auth": "df99a7ab5f64c27fd4bc155c44b452fd",
#     "id": 1
# }
##############################################
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
#     "auth": "df99a7ab5f64c27fd4bc155c44b452fd",
#     "id": 1
# }
# 模板ID: 10001
##############################################
# 获取组信息
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
#     "auth": "df99a7ab5f64c27fd4bc155c44b452fd",
#     "id": 1
# }
# 组ID：2
##############################################
# 创建名为web1的主机，把它加入到Linux Servers组中，使用template os linux模板
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web1",
        "interfaces": [   # 指定使用什么方式临控主机
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
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "df99a7ab5f64c27fd4bc155c44b452fd",
    "id": 1
}



##############################################
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
