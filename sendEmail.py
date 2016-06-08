from email.mime.text import MIMEText
import smtplib
from email.header import Header
# 输入Email地址和口令:
from_addr = 'xxxxx@yeah.net'
password = 'xxxxxx'
# 输入收件人地址:
to_addr = 'xxxxx@gmail.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.yeah.net'
subject = 'title: test send email'
msg = MIMEText('内容:发送成功 from python','plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'diao<xxxx@yeah.net>'
msg['To'] = "xxxxx@gmail.com"
smtp = smtplib.SMTP()
server = smtplib.SMTP(smtp_server,25) # SMTP协议默认端口是25
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()