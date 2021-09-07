from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def f1():
	adst.deiconify()
	root.withdraw()

def f2():
	root.deiconify()
	adst.withdraw()

def f3():
	stdata.delete(1.0,END)  #to bring cursor
	vist.deiconify()
	root.withdraw()
	con = None
	try:
		con = connect("test.db")
		print("connected")
		cursor=con.cursor()
		sql = "select * from student"	
		cursor.execute(sql)
		data=cursor.fetchall() #list of tuples
		info = ""
		for d in data:
			info = info+"rno: "+str(d[0])+"name: " + str(d[1]) + "\n"
		stdata.insert(INSERT,info)	
	except Exception as e:
		print("selection issue ",e)
	finally:
		if con is not None:
			con.close()
			print("disconnected")	
def f4():
	root.deiconify()
	vist.withdraw()
def f5():
	con = None
	try:
		con=connect("test.db")
		print("connecterd")
		rno=int(entrno.get())
		name=entname.get()
		args=(rno,name)
		cursor=con.cursor()
		sql="insert into student values('%d','%s')"
		cursor.execute(sql % args)
		con.commit()
		showinfo("sucess","record added ")
	except Exception as e:
		showerror("failiure","insert issue "+str(e))
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("disconnected")
#design of root window

root = Tk()
root.title("S.M.S")
root.geometry("500x400+400+200")

btnAdd= Button(root,text="Add",font=("arial",18,"bold"),width=10,command=f1)
btnView= Button(root,text="View",font=("arial",18,"bold"),width=10,command=f3)
btnAdd.pack(pady=10)
btnView.pack(pady=10)



#design of adst window

adst = Toplevel(root)
adst.title("Add student")
adst.geometry("500x400+400+200")
adst.withdraw()

lblrno = Label(adst,text="enter rno",font=("arial",18,"bold"))
entrno=Entry(adst,bd=5,font=("arial",18,"bold"))
lblname=Label(adst,text="enter name",font=("arial",18,"bold"))
entname=Entry(adst,bd=5,font=("arial",18,"bold"))
btnsave = Button(adst,text="Save",font=("arial",18,'bold'),command=f5)
btnback=Button(adst,text="Back",font=("arial",18,"bold"),command=f2)

lblrno.pack(pady=5)
entrno.pack(pady=5)
lblname.pack(pady=5)
entname.pack(pady=5)
btnsave.pack(pady=5)
btnback.pack(pady=5)

#design of view window

vist = Toplevel(root)
vist.title("View Student")
vist.geometry("500x400+400+200")
vist.withdraw()

stdata=ScrolledText(vist,width=30,height=20)
btnvback=Button(vist,text="Back",font=("arial",18,"bold"),command=f4)
stdata.pack(pady=10)
btnvback.pack(pady=10)

root.mainloop()
