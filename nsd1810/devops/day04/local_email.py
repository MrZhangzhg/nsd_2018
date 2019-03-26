from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件
message = MIMEText('Python邮件测试\r\n', 'plain', 'utf8')
message['From'] = Header('root@localhost', 'utf8')
message['To'] = Header('bob@localhost', 'utf8')
message['Subject'] = Header('py eamil', 'utf8')

# 发送邮件
sender = 'root@localhost'
receivers = ['root@localhost', 'bob@localhost']
smtp = smtplib.SMTP('localhost')
smtp.sendmail(sender, receivers, message.as_bytes())
