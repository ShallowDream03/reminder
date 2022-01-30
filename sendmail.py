import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail():
    # 设置服务器所需信息
    # qq邮箱服务器地址
    mail_host = 'smtp.qq.com'
    # qq用户名
    mail_user = 'xxxx@qq.com'
    # 密码(部分邮箱为授权码)
    mail_pass = 'xxxx'
    # 邮件发送方邮箱地址
    sender = 'xxxx@qq.com'
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发,可以是任意邮箱地址，不限于QQ
    receivers = ['xxxx@qq.com']

    # 设置email信息
    # 邮件内容设置
    message = MIMEMultipart()
    message.attach(MIMEText('程序崩溃辣', 'plain', 'utf-8'))
    # 邮件主题
    message['Subject'] = '程序崩溃辣'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # file_path=r'C:\Users\pinoz\Desktop\2.png'
    # att = MIMEText(open(file_path,"rb").read(), "base64", "utf-8")
    # att["Content-Type"] = 'application/octet-stream'
    # att["Content-Disposition"] = 'attachment; filename="2.png"'
    # message.attach(att)

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误
        smtpObj.quit()
