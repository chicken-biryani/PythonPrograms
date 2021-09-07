#wapf to find fact of number
def fact1(n):
	f=1
	for i in range(1, n+1):
		f = f * i
	print("Fact = ",f)
fact1(5)

def fact2(n):
	f = 1
	for i in range(1,n+1):
		f = f * i
	return f
ans = fact2(5)
print("Fact = ",ans) 