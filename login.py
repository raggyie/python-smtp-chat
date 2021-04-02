#!/usr/bin/python3

from tkinter import *



#configure the window
def makeLoginGUI():
    tkWindow = Tk()
    tkWindow.configure(bg="black")
    tkWindow.geometry("800x800")
    tkWindow.title("SMTP Chat")
    tkWindow.resizable(FALSE,FALSE)

    #username field
    Label(tkWindow,text="eMail Address", width="20", height="4",bg="black",fg="white", font=("Calibri", 20)).grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow,bg="grey",fg="white", textvariable=username,font=("Calibri", 20)).grid(row=0, column=1)  

    #password field
    passwordLabel = Label(tkWindow,text="Password", bg="black",fg="white",width="20", height="4", font=("Calibri", 20)).grid(row=5, column=0)  
    password = StringVar()
    passwordEntry = Entry(tkWindow, bg="grey",fg="white",textvariable=password, show='*', font=("Calibri", 20)).grid(row=5, column=1)  

    #login field
    loginButton = Button(tkWindow, text="Login" , bg="black",fg="white",font=("Calibri", 20)).grid(row=10,column=1)

    #initiate window
    tkWindow.mainloop()
print("Baivab is gay")
makeLoginGUI()
