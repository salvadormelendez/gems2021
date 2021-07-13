#!/usr/bin/env python3

#IMPORT EMAIL LIBRARIES
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#PASSWORD FOR THE SENDING EMAILS
pwd = '@Rl2017!!!'

#SET FROM AND TO EMAIL ADDRESSESS
fromaddr = 'afc.cyberteam@gmail.com'
toaddr = 'afc.cyberteam@gmail.com'

#CREATE EMAIL
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'GEMS 2021 - Student Sent Survey!'
body = 'GEMS 2021 - Student Sent Survey!'
msg.attach(MIMEText(body,'plain'))
#ADD ATTACHMENT (IMAGE)
filename = 'survey.txt'
#file_path = '/home/pi/' + filename
file_path = '/root/Desktop/gems2021/' + filename
attachment = open(file_path, 'rb')
#COMPLETE EMAIL CONFIGURATION
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename = %s' % filename)
msg.attach(part)

#TRY TO SEND THE EMAIL
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, pwd)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print('Email Sent!')
except:
    print('Unable to send email. Try again!')
