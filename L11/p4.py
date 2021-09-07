from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext

root = Tk()
root.title("S. M. S. ")
root.geometry("400x300+300+200")

def f1():
	root.withdraw()
	addst.deiconify()	
def f2():
	addst.withdraw()
	root.deiconify()	
def f3():
	root.withdraw()
	viewst.deiconify()	
	import cx_Oracle
	con = None 
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + "r: " + str(d[0]) + " n: " + str(d[1]) + "\n"
		stData.insert(INSERT , msg)
	except cx_Oracle.DatabaseError as e:
		print("some issue ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def f4():
	viewst.withdraw()
	root.deiconify()	
def f5():
	import cx_Oracle
	con = None 
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		rno = int(entRno.get())
		name = entName.get()
		cursor = con.cursor()
		sql = "insert into student values('%d' , '%s')"
		args = (rno, name)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + " records inserted "
		messagebox.showinfo("Sahi kiya re ",msg)
		entRno.delete(0, END)
		entName.delete(0, END)
		entRno.focus()
	except cx_Oracle.DatabaseError as e:
		messagebox.showerror("Galat kiya re ", e)
		con.rollback()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

btnAdd = Button(root, text="Add",font=("arial", 18,"bold"), width = 10, command=f1)
btnView = Button(root, text="View",font=("arial", 18,"bold"), width = 10, command=f3)

btnAdd.pack(pady=10)
btnView.pack(pady=10)

addst = Toplevel(root)
addst.title("Add S")
addst.geometry("400x300+300+200")
addst.withdraw()
lblRno = Label(addst, text="enter rno ",font=("arial", 18,"bold"))
entRno = Entry(addst, bd=5,font=("arial", 18,"bold"))
lblName = Label(addst, text="enter name ",font=("arial", 18,"bold"))
entName= Entry(addst, bd=5,font=("arial", 18,"bold"))
btnAddSave = Button(addst, text="Save",font=("arial", 18,"bold"),command=f5)
btnAddBack = Button(addst, text="Back",font=("arial", 18,"bold"),command=f2)

lblRno.pack(pady=5)
entRno.pack(pady=5)
lblName.pack(pady=5)
entName.pack(pady=5)
btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

viewst = Toplevel(root)
viewst.title("View S")
viewst.geometry("400x300+300+200")
viewst.withdraw()

stData = scrolledtext.ScrolledText(viewst, width=40,height=10)
btnViewBack = Button(viewst, text="Back",font=("arial", 18,"bold"),command=f4)

stData.pack()
btnViewBack.pack()

root.mainloop()


























			

































		