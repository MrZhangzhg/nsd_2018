from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

message = MIMEText('Python邮件测试\r\n', 'plain', 'utf8')
message['From'] = Header('zhangzhigang79@126.com', 'utf8')
message['To'] = Header('root@localhost', 'utf8')
message['Subject'] = Header('Welcome', 'utf8')
password = getpass.getpass()

smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
# smtp.starttls()   # 如果服务器要求安全通信，打开此注释
smtp.login('zhangzhigang79@126.com', password)
sender = 'zhangzhigang79@126.com'
receivers = ['zhangzhigang79@126.com']
smtp.sendmail(sender, receivers, message.as_bytes())
