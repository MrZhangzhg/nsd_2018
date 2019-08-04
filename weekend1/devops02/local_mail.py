from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件
messge = MIMEText('Hello from python\r\n', 'plain', 'utf8')
messge['From'] = Header('root', 'utf8')
messge['To'] = Header('bob', 'utf8')
messge['Subject'] = Header('py mail')

# 发邮件
smtp = smtplib.SMTP('127.0.0.1')
smtp.sendmail('root', ['root', 'bob'], messge.as_bytes())
