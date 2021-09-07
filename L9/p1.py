#wapp to perform follow op:
#i/p: 10 add 20
#and / sub / mul / div
try:
	operation = input("Sepcify the expression ")
	expression = operation.split(" ")
	op1 = int(expression[0])
	operator = expression[1]
	op2 = int(expression[2])

	if operator == "add":
		res = op1 + op2
		
	elif operator == "sub" :
		res = op1 - op2
		
	elif operator == "mul" :
		res = op1 * op2
		
	elif operator == "div" :
		res = op1 / op2
			
	else:
		print("invalid operator ")
except IndexError:
	print("expression is incomplete ")
except ValueError:
	print("integers are excepted")
except ZeroDivisionError:
	print("2nd number should not be 0 ")
except Exception as e:	
	print("some other issue ")
	print(e)
	print(e.__class__.__name__)
else:
	print("res = ",res)
	


























