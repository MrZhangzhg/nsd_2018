import requests
import json
import sys

def ding_talk(url, content):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": [
                "15081267865"
            ],
            "isAtAll": False
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()


if __name__ == '__main__':
    url = '钉钉机器人的webhook地址'
    content = sys.argv[1]
    print(ding_talk(url, content))
