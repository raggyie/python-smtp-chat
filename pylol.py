
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image 
from tkinter import messagebox
import smtplib
from tkinter.scrolledtext import ScrolledText

import time
from timeloop import Timeloop
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart

from datetime import timedelta
import re 
import emailpy
import smtplib
import time
import imaplib
import email
import easygui
import traceback 


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

tl=Timeloop()

root = tk.Tk()

username_array=[]
email_array=[]
mode=1
messages=[]
current_email=""

def Login():

        import easyimap
        global messages
        email_entry=email.get()
        password_entry=password.get()
        print(email_entry,password_entry)


        def add_contact():
            def add_contact_tofile():  
                file1 = open("contacts.txt", "a")  # append mode
                file1.write(username_entry.get()+":"+email_entry.get()+"\n")
                file1.close()       
                contact_window.destroy()     

            contact_window=tk.Tk()
            contact_window.title('Add Contact')
            contact_window.geometry('400x300')
            contact_window.maxsize(400,300)
            contact_window.minsize(400,300)
            contact_header = Label(contact_window,bg="orange",width=300,height=2)
            contact_header.place(x=0,y=0)
            email_contact = Label(contact_window,text="Email Address",font= ('verdana',10,'bold'))
            email_contact.place(x=100,y=70)
            email_entry = Entry(contact_window,width=30,relief=RIDGE,borderwidth=3)
            email_entry.place(x=100,y=100)
            username = Label(contact_window,text="Username",font= ('verdana',10,'bold'))
            username.place(x=100,y=130)
            username_entry = Entry(contact_window,width=30,relief=RIDGE,borderwidth=3)
            username_entry.place(x=100,y=160)
            add = Button(contact_window,text="Add Contact",padx=30,bg="orange",relief=RIDGE,borderwidth=1,font= ('verdana',10,'bold'),cursor="hand2",command=add_contact_tofile)
            add.place(x=135,y=200)
            close = Button(contact_window,text="Close",padx=30,bg="orange",relief=RIDGE,borderwidth=1,font= ('verdana',10,'bold'),cursor="hand2")
            close.place(x=160,y=240)
            contact_window.mainloop()
  
        e="baivabatemychips@gmail.com"
        p="Incorrect@0"
     
        if '@gmail.com' not in e  or e == "" :
                messagebox.showerror('Login error',"PLease Write the Valid Email")
        elif p == "":
                 messagebox.showerror('Login error',"   Password Shouldn't be Empty")
        
        else:


                
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls()
            s.login(e,p) #attempt to log into smtp server
            messagebox.showinfo("Login Success","You have Logged to Gmail Successfully")

            filepath = 'contacts.txt'
            with open(filepath) as fp:
                line = fp.readline()
                while line:
                    us=line.split(":")[1]
                    em=line.split(":")[0]
                    global username_array
                    global email_array
                    username_array.append(us)
                    email_array.append(em)
                    
                    
                    line = fp.readline()

                    
            
            root = tk.Tk()
            root.title("E-mail Chat Messenger App")
            root.geometry('900x700')

            def Logout():
                    s.quit()
                    root.destroy()



            header1 = Label(root,bg="orange",width=300,height=2)
            header1.place(x=0,y=0)

            h2 = Label(root,text="Email Chat Messenger",bg="orange",fg="black",font= ('verdana',13,'bold'))
            h2.place(x=175,y=5)
            
            logout = Button(root,text="Logout",padx=20,bg="orange",relief=RIDGE,borderwidth=1,font= ('verdana',10,'bold'),cursor="hand2",command=Logout)
            logout.place(x=390,y=38)



            frame1 = tk.Frame(root)
            frame2 = tk.Frame(root)
        
            

            frame1.grid(row=0, column=0, sticky="nsew")
            frame2.grid(row=0, column=1, sticky="nsew")


            root.grid_columnconfigure(0, weight=1, uniform="group1")
            root.grid_columnconfigure(1, weight=4, uniform="group1")
            root.grid_rowconfigure(0, weight=1)
            
            chatlog = tk.Text(frame2, height=35, state=tk.DISABLED)
            userIn = tk.Entry(frame2,width=80)




            @tl.job(interval=timedelta(seconds=1))
            def receive():
                import email
                global messages,e,p
                global username_array,email_array
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
                           
                                for part in msg.walk():
                                    if part.get_content_type() == 'text/plain':
                                        return [email_subject,email_from,part.get_payload()]

                    except Exception as e:
                        traceback.print_exc() 
                        print(str(e))


                if(mode==1):
                    k=read_email_from_gmail()
     
                    



   
                    

                    lst = re.findall('\S+@\S+', k[1])     
                        
                   

      
                  
                    print(k)
                    if(k[0]=="smtpchat" and lst[0]=="<"+current_email+">" and k[2].rstrip().strip() not in messages):
                        p=-1
                        for i in email_array:
                            p=p+1
                            if(i==current_email):
                                break
                        print("match")
                        chatlog.config(state=tk.NORMAL)        
                        chatlog.insert(tk.END, username_array[p]+" : "+k[2].rstrip().strip()+"\n")
                        messages.append(k[2].rstrip().strip())
                        chatlog.config(state=tk.DISABLED)
                else:
                    k=read_email_from_gmail()
                    lst = re.findall('\S+@\S+', k[1])     
                        
                   

      
               

                    if(k[0]=="smtpgroupchat"   and k[2].rstrip() not in messages):
                        p=-1
                        for i in email_array:
                            p=p+1
                            lst = re.findall('\S+@\S+', k[1])   
                            if("<"+i+">"==lst[0]):
                                break
                        if p==-1:
                            chatlog.config(state=tk.NORMAL)        
                            chatlog.insert(tk.END, k[1]+" : "+k[2].rstrip()+"\n")
                            messages.append(k[2].rstrip())
                            chatlog.config(state=tk.DISABLED)
                        else:    

                            chatlog.config(state=tk.NORMAL)        
                            chatlog.insert(tk.END, username_array[p]+" : "+k[2].rstrip()+"\n")
                            messages.append(k[2].rstrip())
                            chatlog.config(state=tk.DISABLED)



                # mail = imaplib.IMAP4_SSL(SMTP_SERVER)
                # mail.login(FROM_EMAIL,FROM_PWD)
                # mail.select('inbox')
                # data = mail.search(None, 'ALL')
                # mail_ids = data[1]
                # id_list = mail_ids[0].split()   
                # latest_email_id = int(id_list[-1])

                # data = mail.fetch(str(latest_email_id), '(RFC822)' )
                # for response_part in data:
                #     arr = response_part[0]
                #     if isinstance(arr, tuple):
                #         msg = email.message_from_string(str(arr[1],'utf-8'))
                #         email_subject = msg['subject']
                #         email_from = msg['from']
                #         print('From : ' + email_from + '\n')
                #         print('Subject : ' + email_subject + '\n')
                #         if mode==1:    
                #             # if(email_from==email):
                #             p=-1
                #             for i in email_array:
                #                 p=p+1
                #                 if(i==mail.sender):
                #                     break
                #             for part in msg.walk():
                #                 if part.get_content_type() == 'text/plain':
                #                     chatlog.config(state=tk.NORMAL)        
                #                     chatlog.insert(tk.END, "\n"+username_array[p]+" : "+part.get_payload())
                #                     messages.append(mail.body)
                #                     chatlog.config(state=tk.DISABLED)        


        







                # manager = emailpy.EmailManager(e, p)
                # mes = manager.read()
                # print(e.p)
                # for m in mes:
                #     print(m)
                #     if m.sender==current_email and m.body not in messages:
                #         chatlog.config(state=tk.NORMAL)
                #         p=-1
                #         for i in email_array:
                #             p=p+1
                #             if(i==mail.sender):
                #                 break
                        
                #         chatlog.insert(tk.END, "\n"+username_array[p]+" : "+mail.body.strip())
                #         messages.append(mail.body)
                #         chatlog.config(state=tk.DISABLED)
                #         print(type(message.attachment))
                    
                    # for attachment in message.attachments:
                    #     print(attachment.name)
                    #     attachment.download()







                  
                # mail=imapper.mail(imapper.listids()[0])

                # global email
                # global email_array
                # global username_array
                # if(mail.title=="smtpchat"):
                #     print("one",mail,email)
                   
                #     if(mail.body not in messages and mail.From==email):
                #         chatlog.config(state=tk.NORMAL)
                #         print("two")
                #         p=-1
                #         for i in email_array:
                #             p=p+1
                #             if(i==mail.sender):
                #                 break
                    
                #         chatlog.insert(tk.END, "\n"+username_array[p]+" : "+mail.body.strip())
                #         messages.append(mail.body)
                        
                    

                #         chatlog.config(state=tk.DISABLED)


                 
                # elif(mail.title=="smtpgroupchat"):
                #     print(mail.body)
                    
                #     if(mail.body not in messages):
                #         chatlog.config(state=tk.NORMAL)
               
                #         p=-1
                #         for i in email_array:
                #             p=p+1
                #             if(i==mail.sender):
                #                 break
                #         if(p==-1):
                #             chatlog.insert(tk.END, "\n"+mail.sender+" : "+mail.body.strip())
                #         else:    
                #             chatlog.insert(tk.END, "\n"+username_array[p]+" : "+mail.body.strip())
                #         messages.append(mail.body)
                        
                    

                #         chatlog.config(state=tk.DISABLED)       


                        
            def Send_Document():

                doc_path=easygui.fileopenbox()
         
                port=465
                #obtain receiver from gui 
                sslcontext=ssl.create_default_context()
                connection = smtplib.SMTP_SSL("smtp.gmail.com",port,context=sslcontext)
                connection.login(e,p)
                msg = MIMEMultipart()
                msg['From'] = e
                msg['To'] = current_email
                msg['Subject'] = 'smtpchat'
                body = 'YOUR TEXT'
                



                pdfname = doc_path
           
                binary_pdf = open(pdfname, 'rb')
                
                payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                payload.set_payload((binary_pdf).read())
  
                encoders.encode_base64(payload)

                payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                msg.attach(payload)
               
                print(e,p)
    
            
                connection.sendmail(e,current_email,msg.as_string())
                chatlog.config(state=tk.NORMAL)
                
                chatlog.insert(tk.END, "\nMe : "+"Sent a Document")
                

                chatlog.config(state=tk.DISABLED)
                
            def Send():
                global current_email
                global username_array
                message=userIn.get()
                if  message:
                    if mode==1:
                        
                        #obtain all these fields from the gui
                        port=465
                        #obtain receiver from gui 
                        sslcontext=ssl.create_default_context()
                        connection = smtplib.SMTP_SSL("smtp.gmail.com",port,context=sslcontext)
                        connection.login(e,p)
                        msg = MIMEMultipart()
                        msg['From'] = e
                        msg['To'] = current_email
                        msg['Subject'] = 'smtpchat'
                        body = 'YOUR TEXT'
                        msg.attach(MIMEText(message,'plain'))
                        print(e,p)
            
                    
                        connection.sendmail(e,current_email,msg.as_string())
                        chatlog.config(state=tk.NORMAL)
                        
                        chatlog.insert(tk.END, "\nMe : "+message)
                        

                        chatlog.config(state=tk.DISABLED)
                    else:
                        
                        
                        #obtain all these fields from the gui
                        port=465
                        #obtain receiver from gui 
                        sslcontext=ssl.create_default_context()
                        connection = smtplib.SMTP_SSL("smtp.gmail.com",port,context=sslcontext)
                        connection.login(e,p)
                        global email_array
                        for k in email_array:
                            
                            msg = MIMEMultipart()
                            msg['From'] = e
                            msg['To'] = k
                            msg['Subject'] = 'smtpgroupchat'
                            body = 'YOUR TEXT'
                            msg.attach(MIMEText(message,'plain'))
                            print(e,p)
                           
                           

                            connection.sendmail(e,k,msg.as_string())
                        chatlog.config(state=tk.NORMAL)
                        
                        chatlog.insert(tk.END, "\nMe : "+message)
                        

                        chatlog.config(state=tk.DISABLED)


    
            send = tk.Button(frame2, text="Send Message",command=Send)
            send_doc = tk.Button(frame2, text="Send Document",command=Send_Document)
            #addcontact_button = tk.Button(frame2, text="Add Contact")
            
            chatlog.pack()
            userIn.pack()
            send.pack()
            send_doc.pack()
            #addcontact_button.pack()


           
            contactlog = tk.Text(frame1, height=35, width = 38 )
         
            contactlog.insert(tk.END, "Contacts List \n\n",'bold')
            contactlog.insert(tk.END, "1.Group Chat" + "\n")
            t=2
            for k in username_array:
                contactlog.insert(tk.END,str(t)+"."+k.strip()+"\n")
                t=t+1
            #contactlog.insert(tk.END, "2.Bob" + "\n")
            contact_input = tk.Entry(frame1, width=25)
            def clear_entry(event, entry):
                contact_input.delete(0, tk.END)
                contact_input.unbind('<Button-1>', click_event)
            
            contact_input.insert(0,"Enter the Contact number")

            
            contact_input.bind("<Button-1>", lambda event: clear_entry(event, contact_input))
            def Connect():
                global mode
                if contact_input.get().isnumeric:
                    k=contact_input.get()
                    chatlog.config(state=tk.NORMAL)
                    chatlog.delete("1.0", tk.END)
                    print(k)
                    if int(k)==1:
                        mode=0
                        chatlog.insert(tk.END, "Group Chat"+"\n")
                       
                    else: 
                        mode=1
                        global current_email
                        current_email=email_array[int(k)-2]
                    
                        chatlog.insert(tk.END, "You are now chatting with "+username_array[int(k)-2]+"\n" )
                    tl.start(block=False)
                    chatlog.config(state=tk.DISABLED)
            add = tk.Button(frame1, text="Connect",command=Connect)
            
    
            contactlog.pack()
            contact_input.pack()
         
            add.pack()

            menubar = Menu(root)  
            menubar.add_command(label="Add Contact",command=add_contact)  
            def Quit():
                root.destroy()

         
            menubar.add_command(label="Quit!",command=Quit)  
            
            # display the menu  
            root.config(menu=menubar)  

           
       
            def Quit():
                root.destroy()

         



                    
 



            #send = Button(root,text="Send",padx=30,relief=RIDGE,borderwidth=1,bg="orange",font= ('verdana',10,'bold'),cursor="hand2",command=Send)
            #send.place(x=350,y=360)
            root.mainloop()

                                



                                

                                                        
                                
                        # except:
                        #         messagebox.showerror('Login error',"Failed to Login, Either Your Email or Password is Wrong nor You did Enable less secure Apps in gmail Setting")
                                
                        
       
        
                



root.title('Email Instant Messenger')
root.geometry('400x300')
root.maxsize(400,300)
root.minsize(400,300)

header = Label(root,bg="orange",width=300,height=2)
header.place(x=0,y=0)

h1 = Label(root,text="Email Instant Messenger",bg="orange",fg="black",font= ('verdana',13,'bold'))
h1.place(x=135,y=5)

img = ImageTk.PhotoImage(Image.open('gmail.png'))

logo = Label(root,image=img,borderwidth=0)
logo.place(x=150,y=38)


e = Label(root,text="Email Address",font= ('verdana',10,'bold'))
e.place(x=100,y=130)
email = Entry(root,width=30,relief=RIDGE,borderwidth=3)
email.place(x=100,y=150)



p = Label(root,text="Password",font= ('verdana',10,'bold'))
p.place(x=100,y=190)
password = Entry(root,width=30,relief=RIDGE,borderwidth=3)
password.place(x=100,y=210)


login = Button(root,text="Login",padx=30,bg="orange",relief=RIDGE,borderwidth=1,font= ('verdana',10,'bold'),cursor="hand2",command=Login)
login.place(x=135,y=240)



root.mainloop()


