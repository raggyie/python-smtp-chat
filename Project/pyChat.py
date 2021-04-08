import smtplib
import time
import imaplib
import email
import traceback 

ORG_EMAIL = "@gmail.com" 
FROM_EMAIL = "baivabatemychips" + ORG_EMAIL 
FROM_PWD = "Incorrect@0" 
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        latest_email_id = int(id_list[-1])

        data = mail.fetch(str(latest_email_id), '(RFC822)' )
        for response_part in data:
            arr = response_part[0]
            if isinstance(arr, tuple):
                msg = email.message_from_string(str(arr[1],'utf-8'))
                email_subject = msg['subject']
                email_from = msg['from']
                print(msg)
                print('From : ' + email_from + '\n')
                print('Body : ' + email_subject + '\n')
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        print(part.get_payload())

    except Exception as e:
        traceback.print_exc() 
        print(str(e))

read_email_from_gmail()