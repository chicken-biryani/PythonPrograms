from tkinter import *
from tkinter.messagebox import *
from datetime import *
from webbrowser import *
root = Tk()
root.title("D n T App")
root.geometry("500x400+400+200")
root.comfigure(background="sky blue")

def f1():
	dt = datetime.now().date()
	showinfo("date ",dt)
def f2():
	ti=datetime.now().time()
	showwarning("time",ti)
def f3():
	dtti = datetime.now().time()
	showerror("date time",dtti)
def f4():
	open("www.google.com")

btnDate=Button(root,text="Date",width=10,font("times",20,"bold"),command=f1)
btnTime=Button(root,text="Time",width=10,font("times",20,"bold"),command=f2)
btnDateTime = Button(root,text="Date Time",width=10,font=("times",20,"bold"),command=f3)
btnVisitUs=Button(root,text="visit us",width=10,font("times",20,"bold"),command=f4)

btnDate.pack(pady=20)
btnTime.pack(pady=20)
btnDateTime.pack(pady=20)
btnVisitUs.pack(pady=20)
root.mainloop()
