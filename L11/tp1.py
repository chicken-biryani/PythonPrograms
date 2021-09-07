class MU():
	def fic(self):
		print("mu will do the checking")
	@abstractmethod
	def sec(self):
		pass
	def foc(self):
		print("mu will do the checking")
class c1(MU):
	def sec(self):
		print("college will do the checking")

c=c1()
c.fc()
c.sec()
c.foc()