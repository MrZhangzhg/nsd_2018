import requests

url = 'http://127.0.0.1/polls/2/vote/'
data = {'choice_id': '11'}

for i in range(100):
    r = requests.post(url, data=data)
