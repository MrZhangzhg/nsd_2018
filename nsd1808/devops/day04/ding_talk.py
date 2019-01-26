import requests
import json

if __name__ == '__main__':
    url = '你的钉钉机器人地址'
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    # data = {
    #     "msgtype": "text",   # 发送的是文本
    #      "text": {
    #          "content": "我就是我,  @18257185233 是不一样的烟火"
    #      },
    #      "at": {
    #          "atMobiles": [
    #              "18257185233"
    #          ],
    #          "isAtAll": False
    #      }
    # }
    # data = {
    #     "msgtype": "link",
    #     "link": {
    #         "text":"群机器人是钉钉群的高级扩展功能。群机器人可以将第三方服务的信息聚合到群聊中，实现自动化的信息同步。例如：通过聚合GitHub，GitLab等源码管理服务，实现源码更新同步；通过聚合Trello，JIRA等项目协调服务，实现项目信息同步。不仅如此，群机器人支持Webhook协议的自定义接入，支持更多可能性，例如：你可将运维报警提醒通过自定义机器人聚合到钉钉群。",
    #         "title": "自定义机器人协议",
    #         "picUrl": "",
    #         "messageUrl": "https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.Rqyvqo&treeId=257&articleId=105735&docType=1"
    #     }
    # }
    data = {
        "msgtype": "markdown",
        "markdown": {"title":"杭州天气",
            "text":"#### 杭州天气  \n > 9度，@1825718XXXX 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](https://www.seniverse.com/) "
        },
        "at": {
            "atMobiles": [
                "1825718XXXX"
            ],
            "isAtAll": False
        }
     }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print(r.json())
