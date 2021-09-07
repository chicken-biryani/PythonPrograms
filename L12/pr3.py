'''wap to write from cla to find square root of number and 
find squar root'''

import sys
import math
try:
	a=float(sys.argv[1])
	c=math.sqrt(a)
except (IndexError,ValueError):
	print("u need to pass a number ")

else:
	print(c)