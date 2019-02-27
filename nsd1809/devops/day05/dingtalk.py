import requests
import json

def ding_talk(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    # data = {
    #     "msgtype": "text",
    #     "text": {
    #         "content": msg
    #     },
    #     "at": {
    #         "atMobiles": reminders,
    #         "isAtAll": False
    #     }
    # }
    data = {
        "msgtype": "markdown",
        "markdown": {"title":"杭州天气",
            "text":"#### 杭州天气  \n > 9度，@1825718XXXX 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](https://www.seniverse.com) "
        },
        "at": {
            "atMobiles": [
            "1825718XXXX"
        ],
        "isAtAll": False
        }
    }
    r = requests.post(url,headers=headers, data=json.dumps(data))
    return r.json()

if __name__ == '__main__':
    url = '你机器人的webhook地址'
    reminders = ['15678654567']  # @哪些人
    msg = '这是要发送的内容'
    print(ding_talk(url, reminders, msg))
