import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendMail(object):
    '''发送邮件'''
    def __init__(self, sender, username, password, receiver, file_dir):
        self.sender = sender
        self.username = username
        self.password = password
        self.receiver = receiver
        self.file_dir = file_dir

    def send(self):
        with open(self.file_dir, 'rb') as f:
            mail_body = f.read()
        subject = 'today report'
        # 定义邮件内容
        msg = MIMEMultipart()
        msg['Subject'] = Header(subject)
        msg['From'] = self.sender
        msg['To'] = ','.join(self.receiver)
        body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg.attach(body)
        # 添加附件
        att = MIMEText(mail_body, _subtype='base64', _charset='utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="my_report.html"'
        msg.attach(att)
        # 发送邮件
        email_host = 'smtp.exmail.qq.com'
        smtp = smtplib.SMTP_SSL()
        smtp.connect(email_host, 465)
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, self.receiver, msg.as_string())
        smtp.quit()

if __name__ == '__main__':
    SendMail('nian.zhidan@zyxr.com', 'nian.zhidan@zyxr.com', 'Nzd187', ['nian.zhidan@zyxr.com', '1564043999@qq.com'], '/Users/nianzhidan/PycharmProjects/zyxr_new/report/report0.html').send()

