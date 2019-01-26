from email.mime.text import MIMEText
from email.header import Header
import smtplib

message = MIMEText('Python邮件测试\r\n', 'plain', 'utf8')
message['From'] = Header('linus@kernel.org', 'utf8')
message['To'] = Header('root@localhost', 'utf8')
message['Subject'] = Header('Welcome', 'utf8')

smtp = smtplib.SMTP('localhost')
sender = 'linus@kernel.org'
receivers = ['root@localhost', 'alice@localhost']
smtp.sendmail(sender, receivers, message.as_bytes())
