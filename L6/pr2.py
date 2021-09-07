#read sentence from user and creat a new sentence
#which would have each word sorted 

def mysort(s):
	d=sorted(s)
	a=''.join(d)
	return a


s=input("enter string ")

data=s.split(' ')
a=""
for d in data:
	n=d
	a=a+' '+mysort(d)
	
print("orignal is ",s,"modified ",a)

