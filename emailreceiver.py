#!/usr/bin/python3

import easyimap as e
     

username = "baivabatemychips@gmail.com"
password = "Incorrect@0"

server=e.connect("imap.gmail.com",username,password)
email=server.mail(server.listids()[0])

print(email.body)


    