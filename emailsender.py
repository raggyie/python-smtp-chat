#!/usr/bin/python3

import smtplib, ssl

username = "baivabatemychips@gmail.com"
password = "Incorrect@0"


message="""/

this message is from python

from baivab ate my chips

"""

port=465


receiver = "raghavendrasureshk10@gmail.com"

sslcontext=ssl.create_default_context()

connection = smtplib.SMTP_SSL("smtp.gmail.com",port,context=sslcontext)

connection.login(username,password)

connection.sendmail(username,receiver,message)

print("your message is sent")


