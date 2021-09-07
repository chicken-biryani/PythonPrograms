'''this program covers concepts of different message boxes in tkinter ,web browsing ,datetime package,and tkinter'''
from tkinter import *
from tkinter.messagebox import *
from datetime import *
from webbrowser import *

#the framework of the tkinter application
root = Tk()
root.title("Date and Time")
root.geometry("500x400+400+200") 
root.configure(background="sky blue")

#The functions 
def f1(): #for date
	dt = datetime.now().date()
	showinfo("Date ",dt) #this gives a 
def f2(): #funtion for time
	ti=datetime.now().date()
	showwarning("Time",ti) #this gives a warning message box pop up
def f3(): #funtion for date and time
	dtti = datetime.now()
	showerror("Date Time ",dtti) #this is gives an error message box pop up
def f4(): #function for google
	open("www.google.com")

#making of the buttons
btnDate=Button(root,text="Date",width=10,font=('times',20,'bold'),command=f1)
btnTime=Button(root,text="Time",width=10,font=('times',20,'bold'),command=f2)
btnDateTime=Button(root,text="Date Time",width=10,font=('times',20,'bold'),command=f3)
btnGoogle=Button(root,text="Google",width=10,font=('times',20,'bold'),command=f4)

#displaying of the buttons
btnDate.pack(pady=20)
btnTime.pack(pady=20)
btnDateTime.pack(pady=20)
btnGoogle.pack(pady=20)

root.mainloop()