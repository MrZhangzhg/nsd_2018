import json
import requests
import getpass

def dingtalk(url):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
    "msgtype": "link",
    "link": {
        "text": "这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？",
        "title": "时代的火车向前开",
        "picUrl": "https://upload.jianshu.io/users/upload_avatars/12347101/6b21f2d2-de50-4c8f-ba23-bf7f80ba77aa.jpg",
        "messageUrl": "http://www.tmooc.cn"
    }
}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.json()

if __name__ == '__main__':
    # url = '此处填写webhook的内容'
    url = getpass.getpass()
    print(dingtalk(url))
