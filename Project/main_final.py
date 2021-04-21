
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

import easyimap
import easygui
import traceback 


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import threading
from time import sleep


tl=Timeloop()

e=""
p=""


email=""
password=""

username_array=[]
email_array=[]
mode=1
messages=[]
current_email=""


class Contact():

    #module used for adding contacts to contact.txt

    def __init__(self):
        
        self.contact_window=tk.Tk()
        self.contact_window.title('Add Contact')
        self.contact_window.geometry('400x300')
        #contact_window.maxsize(400,300)
        #contact_window.minsize(400,300)
        self.contact_window.resizable(FALSE,FALSE)
        contact_header = Label(self.contact_window,bg="orange",width=300,height=2)
        contact_header.place(x=0,y=0)
        email_contact = Label(self.contact_window,text="Email Address",font= ('verdana',10,'bold'))
        email_contact.place(x=100,y=70)
        self.email_entry = Entry(self.contact_window,width=30,relief=RIDGE,borderwidth=3)
        self.email_entry.place(x=100,y=100)
        username = Label(self.contact_window,text="Username",font= ('verdana',10,'bold'))
        username.place(x=100,y=130)
        self.username_entry = Entry(self.contact_window,width=30,relief=RIDGE,borderwidth=3)
        self.username_entry.place(x=100,y=160)
        add = Button(self.contact_window,text="Add Contact",padx=30,bg="orange",relief=RIDGE,borderwidth=1,font= ('verdana',10,'bold'),cursor="hand2",command=self.add_contact_tofile)
        add.place(x=135,y=200)
        close = Button(self.contact_window,text="Close",padx=30,bg="orange",relief=RIDGE,borderwidth=1,font= ('verdana',10,'bold'),cursor="hand2")
        close.place(x=160,y=240)
        self.contact_window.mainloop()

    def add_contact_tofile(self):  
            file1 = open("contacts.txt", "a")  # append mode
            file1.write(self.email_entry.get()+":"+self.username_entry.get()+"\n")
            file1.close()       
            self.contact_window.destroy() 
    
    def add_contact():
        contact=Contact() 
   

class Login():
    def __init__(self):

            #root is the window's name
            root = tk.Tk()
            root.title("E-mail Chat Messenger App")
            root.geometry('400x300')
            root.resizable(FALSE,FALSE)
            root.title('Email Instant Messenger')
            #adding gui components to the window
            header = Label(root,bg="orange",width=300,height=2)
            header.place(x=0,y=0)
            h1 = Label(root,text="Email Instant Messenger",bg="orange",fg="black",font= ('verdana',13,'bold'))
            h1.place(x=135,y=0)
            tempimg=Image.open('gmail.png')
            img = ImageTk.PhotoImage(tempimg)
            logo = Label(root,image=img,borderwidth=0)
            logo.place(x=150,y=38)
            e = Label(root,text="Email Address",font= ('verdana',10,'bold'))
            e.place(x=100,y=130)
            #email and password entries
            global email,password
            email = Entry(root,width=30,relief=RIDGE,borderwidth=3)
            email.place(x=100,y=150)
            p = Label(root,text="Password",font= ('verdana',10,'bold'))
            p.place(x=100,y=190)
            password = Entry(root,width=30,relief=RIDGE,borderwidth=3)
            password.place(x=100,y=210)
            login = Button(root,text="Login",padx=30,bg="orange",relief=RIDGE,borderwidth=1,font= ('verdana',10,'bold'),cursor="hand2",command=Login.login_process)
            login.place(x=135,y=240)
            #launch window
            root.mainloop()
            Login.login_process()
    @staticmethod
    def login_load(email,password):

        global messages
        email_entry=email.get()
        password_entry=password.get()
        print(email_entry,password_entry)
        global e
        global p
        e=email_entry
        p=password_entry
    
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

            #~~~~~~~need fix ~~~~~~~~~~~~~~~
            global main
            main=Chat_window()
            #~~~~~~need fix we need to make this global to be accessible to Send_Receive class ~~~~~~~~~~~~
            
    @staticmethod
    def login_process():
        k= Login.login_load(email,password)  

    global e,p,main         
        
sr=None

class Chat_window:
    def __init__(self):

        # ~~~~~~~~ CREATING THE WINDOW ~~~~~~~~~~~~~~~~


        root = tk.Tk()
        root.title("E-mail Chat Messenger App")
        root.geometry('900x700')
        root.resizable(FALSE,FALSE)

        header1 = Label(root,bg="orange",width=300,height=2)
        header1.place(x=0,y=0)

        h2 = Label(root,text="Email Chat Messenger",bg="orange",fg="black",font= ('verdana',13,'bold'))
        h2.place(x=175,y=5)
        
        logout = Button(root,text="Logout",padx=20,bg="orange",relief=RIDGE,borderwidth=1,font= ('verdana',10,'bold'),cursor="hand2",command=Chat_window.Logout)
        logout.place(x=390,y=38)



        frame1 = tk.Frame(root)
        frame2 = tk.Frame(root)
    
        

        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=1, sticky="nsew")


        root.grid_columnconfigure(0, weight=1, uniform="group1")
        root.grid_columnconfigure(1, weight=4, uniform="group1")
        root.grid_rowconfigure(0, weight=1)
        root.configure()

        self.chatlog = tk.Text(frame2, height=35, state=tk.DISABLED)

        self.userIn = tk.Entry(frame2,width=80)
        global sr 
        sr=p2p_Send_Receive(self,e,p)

        
        send = tk.Button(frame2, text="Send Message",command=sr.Send)
        send_doc = tk.Button(frame2, text="Send Document",command=sr.Send_Document)
        #addcontact_button = tk.Button(frame2, text="Add Contact")
        
        self.chatlog.pack()
        self.userIn.pack()
        send.pack()
        send_doc.pack()
        #addcontact_button.pack()


    
        self.contactlog = tk.Text(frame1, height=35, width = 38 )
    
        self.contactlog.insert(tk.END, "Contacts List \n\n",'bold')
        self.contactlog.insert(tk.END, "1.Group Chat" + "\n")
        t=2
        for k in username_array:
            self.contactlog.insert(tk.END,str(t)+"."+k.strip()+"\n")
            t=t+1
        #contactlog.insert(tk.END, "2.Bob" + "\n")
        self.contact_input = tk.Entry(frame1, width=25)
        def clear_entry(event, entry):
            self.contact_input.delete(0, tk.END)
            self.contact_input.unbind('<Button-1>',click_event)
        
        self.contact_input.insert(0,"Enter the Contact number")

        
        self.contact_input.bind("<Button-1>", lambda event: clear_entry(event, self.contact_input))

        
        



        def Connect():
            global mode
            if self.contact_input.get().isnumeric:
                k=self.contact_input.get()
                self.chatlog.config(state=tk.NORMAL)
                self.chatlog.delete("1.0", tk.END)
                print(k)
                if int(k)==1:
                    #group chat mode
                    mode=0
                    self.chatlog.insert(tk.END, "Group Chat"+"\n")
                
                else: 
                    mode=1
                    global current_email
                    current_email=email_array[int(k)-2]
                
                    self.chatlog.insert(tk.END, "You are now chatting with "+username_array[int(k)-2]+"\n" )
                tl.start(block=False)
                #threading._start_new_thread(sr.listen())
                self.chatlog.config(state=tk.DISABLED)
        add = tk.Button(frame1, text="Connect",command=Connect)
        

        self.contactlog.pack()
        self.contact_input.pack()
    
        add.pack()

        menubar = Menu(root)  
        menubar.add_command(label="Add Contact",command=Contact.add_contact)  
        def Quit():
            root.destroy()

    
        menubar.add_command(label="Quit!",command=Quit)  
        
        # display the menu  
        root.config(menu=menubar)

        root.mainloop()  


    
    def Logout(self):
            s.quit()
            root.destroy()
    



         
class p2p_Send_Receive:
    def __init__(self,main,e,p):
        #the instance of the chat window
        self.main=main
        self.e=e
        self.p=p

    @tl.job(interval=timedelta(seconds=1))    
    def listen():
        sr.receive()

            
            
    
    #@tl.job(interval=timedelta(seconds=1))
    def receive(self):
        import email
        global messages
        #global username_array,email_array, self.SMTP_SERVER, self.FROM_EMAIL,self.FROM_PWD
        ORG_EMAIL = "@gmail.com" 

        # !~for development ONLY~!

        self.FROM_EMAIL = self.e 
        self.FROM_PWD = self.p
        self.SMTP_SERVER = "imap.gmail.com" 
        SMTP_PORT = 993



        if(mode==1):
            k=self.read_email_from_gmail()

            

            #lst = re.findall('\S+@\S+', k[1])     
                
        


        
            print(k)

            print("abracadabra")
            if(k[0]=="smtpchat" and k[1]==current_email and k[2].rstrip().strip() not in messages):
                print("we are inside")

                p=-1
                for i in email_array:
                    p=p+1
                    if(i==current_email):
                        break
                print("match")
                self.main.chatlog.config(state=tk.NORMAL)

                #inserting into the window
                self.main.chatlog.insert(tk.END,"\n"+username_array[p].rstrip().strip()+" : "+k[2].rstrip()+"\n")


                messages.append(k[2].rstrip().strip())
                self.main.chatlog.config(state=tk.DISABLED)
        else:
            #read for group chat


            k=self.read_email_from_gmail()
     
                
        

            if(k[0]=="smtpgroupchat"   and k[2].rstrip() not in messages):
                #number of people variable 
                p=-1

                #to identify how many emails are present in your group
                for i in email_array:
                    p=p+1
                    lst = re.findall('\S+@\S+', k[1])   
                    if("<"+i+">"==lst[0]):
                        break
                #if no one are there
                if p==-1:
                    self.main.chatlog.config(state=tk.NORMAL)        
                    self.main.chatlog.insert(tk.END, k[1]+" : "+k[2].rstrip()+"\n")
                    messages.append(k[2].rstrip())
                    self.main.chatlog.config(state=tk.DISABLED)
                else:    
                    self.main.chatlog.config(state=tk.NORMAL)        
                    self.main.chatlog.insert(tk.END, "\n"+username_array[p].rstrip().strip()+" : "+k[2].rstrip()+"\n")
                    messages.append(k[2].rstrip())
                    self.main.chatlog.config(state=tk.DISABLED)



    
    def read_email_from_gmail(self):
        try:
            import email as emailmodule
            mail = imaplib.IMAP4_SSL(self.SMTP_SERVER)
            mail.login(self.FROM_EMAIL,self.FROM_PWD)
            mail.select('inbox')
            data = mail.search(None, 'ALL')
            mail_ids = data[1]
            id_list = mail_ids[0].split()
            #obtain the latest email to display on chat   
            latest_email_id = int(id_list[-1])
            #metthod of fetching the email
            data = mail.fetch(str(latest_email_id), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = emailmodule.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
            
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            return [email_subject,email_from,part.get_payload()]

        except Exception as e:
            traceback.print_exc() 
            print(str(e))

            
    def Send_Document(self):

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
        self.main.chatlog.config(state=tk.NORMAL)
        
        self.main.chatlog.insert(tk.END, "\nMe : "+"Sent a Document")
        

        self.main.chatlog.config(state=tk.DISABLED)


        
    def Send(self):
        global current_email
        global username_array
        message=self.main.userIn.get()
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
                self.main.chatlog.config(state=tk.NORMAL)
                
                self.main.chatlog.insert(tk.END, "\nMe : "+message)
                

                self.main.chatlog.config(state=tk.DISABLED)
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
                self.main.chatlog.config(state=tk.NORMAL)
                
                self.main.chatlog.insert(tk.END, "\nMe : "+message)
                

                self.main.chatlog.config(state=tk.DISABLED)

class group_Send_Receive:
    def __init__(self,main):
        self.main=main


    def Send(self):
        global current_email
        global username_array
        message=self.main.userIn.get()
        if  message:
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
            self.main.chatlog.config(state=tk.NORMAL)
            
            self.main.chatlog.insert(tk.END, "\nMe : "+message)
            

            self.main.chatlog.config(state=tk.DISABLED)
                    
            
        
    

    def receive(self):
        import email
        global messages
        #global username_array,email_array, self.SMTP_SERVER, self.FROM_EMAIL,self.FROM_PWD
        ORG_EMAIL = "@gmail.com" 

        # !~for development ONLY~!

        self.FROM_EMAIL = e 
        self.FROM_PWD = p
        self.SMTP_SERVER = "imap.gmail.com" 
        SMTP_PORT = 993




            #read for group chat


        k=read_email_from_gmail()
        lst = re.findall('\S+@\S+', k[1])     
            
    

        if(k[0]=="smtpgroupchat"   and k[2].rstrip() not in messages):
            #number of people variable 
            p=-1

            #to identify how many emails are present in your group
            for i in email_array:
                p=p+1
                lst = re.findall('\S+@\S+', k[1])   
                if("<"+i+">"==lst[0]):
                    break
            #if no one are there
            if p==-1:
                self.main.chatlog.config(state=tk.NORMAL)        
                self.main.chatlog.insert(tk.END, k[1]+" : "+k[2].rstrip()+"\n")
                self.messages.append(k[2].rstrip())
                self.main.chatlog.config(state=tk.DISABLED)
            else:    
                self.main.chatlog.config(state=tk.NORMAL)        
                self.main.chatlog.insert(tk.END, username_array[p]+" : "+k[2].rstrip()+"\n")
                self.messages.append(k[2].rstrip())
                self.main.chatlog.config(state=tk.DISABLED)                
              

run=Login()