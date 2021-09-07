'''wap to acess command line args
and read two integers
and perfor n1/n2'''

import sys
try:
	a=int(sys.argv[1])
	b=int(sys.argv[2])
	c=a/b
except IndexError:
	print("u need to pass 2 integers")
except ValueError:
	print("pass integers na")
except ZeroDivisionError:
	print("second number should not be 0 ")
else:
	print(c)
