class car:
	company_name="maruto"
	def __init__(self,n,c,price,length): #self obj ka refrence 
		self.name=n #init is also called constructor
		self.color=c
		self.price=price
		self.length=length
	def info(self):
		print("name ",self.name)
		print("clolr",self.color)
		print("price",self.price)
		print("length",self.length)
		print(self.company_name)
		print(car.company_name)
	@staticmethod
	def show_company_name():
		print(car.company_name)
	def showcategory(self):
		if self.length < 3600:
			print("city car")
		elif self.length >= 3600 and self.length <= 4500:
			print("compact car ")
		else:
			print("large car ")
	
#every class should have a construct
#process of making a class is encapsulation
	#jaise function banake ke call waise ho

c1=car("swift","red",3.5,3800) 
c1.info() ; c1.show_company_name(); c1.showcategory()
c2=car("alto","blue",2.9,9000)
c2.info()   #c1 and c2 are refrence variables