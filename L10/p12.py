from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Even Odd Calci ")
root.geometry("350x300+300+200")

def f1():
	try:
		n = int(entNumber.get())
		msg = ""
		if n % 2 == 0:
			msg = "Even"
		else:
			msg = "Odd"
		messagebox.showinfo("Jawab",msg)
	except ValueError:
		messagebox.showerror("Galat Kiya","Integers only")
		entNumber.delete(0,END)
		entNumber.focus()
lblNumber = Label(root, text="Enter Number ", font=("arial",18,"bold"))
entNumber = Entry(root, bd=5, font=("arial",18,"bold"))
btnFind = Button(root, text="Find",font=("arial",18,"bold"),command=f1)
lblNumber.pack()
entNumber.pack()
btnFind.pack()
root.mainloop()