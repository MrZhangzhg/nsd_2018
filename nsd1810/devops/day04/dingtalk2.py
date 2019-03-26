import requests
import json
import getpass

def send_msg(url):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "link",
        "link": {
            "text":"NSD1810第五阶段",
            "title": "我的标题",
            "picUrl": "https://upload.jianshu.io/users/upload_avatars/12347101/6b21f2d2-de50-4c8f-ba23-bf7f80ba77aa.jpg",
            "messageUrl": "https://www.jianshu.com/p/a3c62eb71ae3"
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

if __name__ == '__main__':
    url = getpass.getpass()  # 你机器人的token地址
    result = send_msg(url)
    print(result)
