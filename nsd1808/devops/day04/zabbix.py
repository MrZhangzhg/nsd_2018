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
data = {
    "jsonrpc": "2.0",
    "method": "user.get",
    "params": {
        "output": "extend"
    },
    "auth": "ae10101387ba2ef5b224beb18fd5732a",
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
