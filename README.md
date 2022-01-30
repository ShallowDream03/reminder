# reminder
This is a small project that can send an email to alert you when a program running on a remote server crashes.  



This project uses QQmail as an example, you need to apply for SMTP service before using it.  
[How to apply QQ smtp](https://blog.csdn.net/weixin_31176789/article/details/119268339)



Just use it by putting `sendmail.py` file under your code directory and add `from sendmail import sendmail` in the beginning then use it like `example.py` shows.  

sendmail(0):send Normal end to your email  
sendmail(1):send Error end to your email
