from tkinter import *

root = Tk()
root.title("color me")
root.geometry("500x400+400+100")

def r():
	root.configure(background="RED")
def g():
	root.configure(background="LIGHT GREEN")
def b():
	root.configure(background="#0000ff")



btnred=Button(root,text="Red",width=10,font=("arial",18,"bold"),command=r)
btnred.pack(pady=20)
btngreen=Button(root,text="Green",width=10,font=("arial",18,"bold"),commad=g)
btngreen(pady=20)
btnblue=Button(root,text="Blue",width=10,font=("arial",18,"bold"),command=b)
btnblue.pack(pady=20)
root.mainloop()