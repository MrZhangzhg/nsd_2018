from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_mail(text, subject, sender, receivers, mail_host, password):
    message = MIMEText(text, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    smtp = smtplib.SMTP()
    smtp.connect(mail_host)
    # smtp.starttls()   # 如果服务器要求安全通信，打开此注释
    smtp.login(sender, password)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    mail_host = 'smtp.126.com'
    sender = 'zhangzhigang79@126.com'
    password = getpass.getpass()
    receivers = ['zhangzhigang79@126.com']
    subject = 'Welcome to TEDU'
    text = 'Python邮件测试\r\n'
    send_mail(text, subject, sender, receivers, mail_host, password)
