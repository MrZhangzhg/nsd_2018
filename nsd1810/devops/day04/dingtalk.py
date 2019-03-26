import requests
import sys
import json
import getpass

def send_msg(url, msg, reminders=None):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,  # 不@所有人
        },
        "text": {
            "content": msg,  # 消息正文
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

if __name__ == '__main__':
    url = getpass.getpass()  # 你机器人的token地址
    result = send_msg(url, sys.argv[1], reminders=['13311224455'])
    print(result)
