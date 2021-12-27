from tkinter  import *
from tkinter import messagebox
 

def OK():
    username=e1.get()
    password=e2.get()

    if(username =="" and password ==""):
         messagebox.showinfo("","EMAIL")

    elif(username =="banothurakesh.143@gmail.com" and password =="Rakesh1122"):
         messagebox.showinfo("","login success")
         master.option_readfile(input(1))
    else:
        messagebox.showinfo("","Incorrect Username and Password")         
master=Tk()
master.title("login")
master.geometry("300x300")
global e1
global e2
Label(master,text="username").place(x=10, y=10)
Label(master,text="password").place(x=10, y=40)
e1=Entry(master)
e1.place(x=150, y=10)

e2=Entry(master)
e2.place(x=150, y=40)
e2.configure(show="*")

Button(master,text="login",command=OK,height=4,width=6).place(x=10,y=100)
master.mainloop()
