from tkinter import *
from tkinter.messagebox import*

root=Tk()
root.title("first application ")
root.geometry("500x400+400+200") #(wxh+x+y)

def f1():
	showinfo("Msg","Suprabhat")
btnClickMe = Button(root,text="Click me",command=f1)
btnClickMe.pack()

root.mainloop()