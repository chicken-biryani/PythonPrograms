#wapf to find fact of number by recursion
def fact(n):
	if(n ==1):
		return 1
	else:
		return n * fact(n-1)
n = int(input("Enter Number "))
if n < 0 :
	print("b +ve")
elif n == 0  or n == 1 :
	print("Ans = ",1)
else:
	ans=fact(n)
print("Fact = ",ans)