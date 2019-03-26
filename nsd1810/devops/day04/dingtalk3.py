import requests
import json
import getpass

def send_msg(url):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "markdown",
        "markdown": {"title":"杭州天气",
            "text":"## 杭州天气  \n > 9度，@1825718XXXX **西北风1级**，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气]( https://www.seniverse.com) "
        },
        "at": {
            "atMobiles": [
                "1825718XXXX"
            ],
            "isAtAll": False
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

if __name__ == '__main__':
    url = getpass.getpass()  # 你机器人的token地址
    result = send_msg(url)
    print(result)
