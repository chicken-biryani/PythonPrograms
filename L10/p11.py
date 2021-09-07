from tkinter import*
from datetime import*
from tkinter import messagebox
from webbrowser import*

root = Tk()
root.title("Welcome App")
root.geometry("300x200+300+300")

def f1():
	hour = datetime.now().hour
	msg = ""
	if(hour >= 6 and hour < 12):
		msg="Good Morning"
	elif(hour >= 1 and hour < 18):
		msg = "Good Afternoon"
	else:
		msg = "Good Evening"
	messagebox.showinfo("Swagat",msg)

def f2():
	open("www.google.com")
btnClickMe = Button(root, text="Click Me", width=10, command=f1)
btnVisitUs = Button(root, text="Visit Us", width=10, command=f2)
btnClickMe.pack(pady=10)
btnVisitUs.pack(pady=10)
root.mainloop()





