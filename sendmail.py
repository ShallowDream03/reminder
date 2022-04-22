import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmail(x):
    # 设置服务器所需信息
    # qq邮箱服务器地址
    mail_host = 'smtp.qq.com'
    # 密码(qq邮箱为授权码)
    mail_pass = 'xxxx'
    # 邮件发送方邮箱地址（你的QQ邮箱）
    sender = 'xxxx@qq.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发，可以是任意邮箱，不限于QQ
    receivers = ['xxxx@qq.com', "xxxx@gmail.com", "xxxxx@163.com"]

    # 设置email信息
    # 邮件内容设置
    if x==1:
        message = MIMEMultipart()
        message.attach(MIMEText('程序崩溃辣', 'plain', 'utf-8'))
        # 邮件主题
        message['Subject'] = '程序崩溃辣'
        # 发送方信息
        message['From'] = sender
        # 接受方信息
        for receiver in receivers:
            message['To'] = receiver
    else:
        message = MIMEMultipart()
        message.attach(MIMEText('程序正常结束', 'plain', 'utf-8'))
        # 邮件主题
        message['Subject'] = '程序正常结束'
        # 发送方信息
        message['From'] = sender
        # 接受方信息
        for receiver in receivers:
            message['To'] = receiver

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        # 登录到服务器
        smtpObj.login(sender, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误
        smtpObj.quit()
