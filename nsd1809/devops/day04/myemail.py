from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件
message = MIMEText('Python email test.\r\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')
message['To'] = Header('bob', 'utf8')
message['Subject'] = Header('Email Test', 'utf8')

# 发送邮件
smtp = smtplib.SMTP(host='127.0.0.1')
smtp.sendmail('root@tedu.cn', ['root@localhost', 'bob@localhost'], message.as_bytes())
