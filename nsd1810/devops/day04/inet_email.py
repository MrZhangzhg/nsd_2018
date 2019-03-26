from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_mail(text, sender, receivers, subject, host, passwd):
    # 准备邮件
    message = MIMEText(text, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@qq.com']
    subject = 'python邮件测试'
    text = '这是一封邮件测试。收到不用回复\r\n'
    host = 'smtp.126.com'
    passwd = getpass.getpass()
    send_mail(text, sender,receivers, subject, host, passwd)
