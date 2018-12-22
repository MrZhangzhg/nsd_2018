from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

# 正文
message = MIMEText('python邮件测试\r\n', 'plain', 'utf8')  # plain表示纯文本
message['From'] = Header('billgates@microsoft.com', 'utf8')  # 发件人
message['To'] = Header('zhangzhigang79@qq.com', 'utf8')  # 收件人
message['Subject'] = Header('smtp test', 'utf8')  # 主题

sender = 'billgates@microsoft.com'
receivers = ['zhangzhigang79@qq.com', 'root']
smtp = SMTP('localhost')
smtp.sendmail(sender, receivers, message.as_string())
