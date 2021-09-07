class stack:
	def __init__(self):
		self.data = []
	def push(self,ele):
		self.data.append(ele)
		print(ele)
	def pop(self):
		if len(self.data) == 0:
			print("stack is empty")
		else:
			ele = self.data.pop()
			print("popped element ",ele)
	def display(self):
		if len(self.data) == 0:
			print("stack is empty")
		else:
			print("stack -->", self.data)

s = stack()
while True:
	op = int(input("1, push 2, pop , 3 display 4 exit"))
	if op ==1:
		ele =int(input("enter element to push "))
		s.push(ele)
	elif op == 2:
		s.pop()
	elif op == 3:
		s.display()
	elif op == 4:
		break
	else:
		print("invalid option ")