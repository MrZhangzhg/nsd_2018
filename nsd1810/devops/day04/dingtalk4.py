import requests
import json
import getpass

def send_msg(url):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "actionCard": {
            "title": "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
            "text": "![screenshot](@lADOpwk3K80C0M0FoA) \n #### 乔布斯 20 年前想打造的苹果咖啡厅 \n\n Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划",
            "hideAvatar": "0",
            "btnOrientation": "0",
            "singleTitle" : "阅读全文",
            "singleURL" : "https://www.dingtalk.com/"
        },
        "msgtype": "actionCard"
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

if __name__ == '__main__':
    url = getpass.getpass()  # 你机器人的token地址
    result = send_msg(url)
    print(result)
