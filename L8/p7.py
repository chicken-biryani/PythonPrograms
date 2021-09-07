#wapp to access CLA for getting two integers and perform ans = a + b

import sys
try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	ans = a + b
except IndexError:
	print("u need to pass 2 integers ")
except ValueError:
	print("bolana only integers ")
except ZeroDivisionError:
	print("2nd number should not be 0 ")
else:
	print("Ans = ", ans)
finally:
	print("lecture over ")