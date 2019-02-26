from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_email(text, sender, receivers, subject, host, user, passwd):
    message = MIMEText(text, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    smtp = smtplib.SMTP(host)
    # smtp.starttls()  # 如果服务器是需要加密通信的，则打开此注释
    smtp.login(user, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    text = '这是一封python邮件测试\r\n'
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@126.com']
    subject = '邮件测试'
    host = 'smtp.126.com'
    user = 'zhangzhigang79@126.com'
    passwd = getpass.getpass()
    send_email(text, sender, receivers, subject, host, user, passwd)
