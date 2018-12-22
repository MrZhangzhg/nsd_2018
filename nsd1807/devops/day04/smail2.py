from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP
import getpass

def send_mail(text, subject, sender, receivers, server, user, passwd, port=25):
    message = MIMEText(text, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')
    smtp = SMTP()
    smtp.connect(server, port)
    # smtp.starttls()   # 如果使用证书，打开此注释
    smtp.login(user, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    text = 'python邮件测试\r\n'
    subject = 'smtp test'
    sender = 'zhangzhigang79@126.com'
    passwd = getpass.getpass()
    server = 'mail.tedu.cn'
    receivers = ['zhangzhigang79@126.com', 'zhangzhigang79@qq.com']
    send_mail(text, subject, sender, receivers, server, sender, passwd)
