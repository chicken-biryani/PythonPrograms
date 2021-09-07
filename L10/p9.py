'''c1 =  (r1 + r2 + r3 + r4) == 21
	c2 = (r5 + r6 + r7 + r8) == 21
	c3 = (r2 == r6)
'''
import random
while True:
	r1 = random.randrange(10)
	r2 = random.randrange(10)
	r3 = random.randrange(10)
	r4 = random.randrange(10)
	r5 = random.randrange(10)
	r6 = random.randrange(10)
	r7 = random.randrange(10)
	r8 = random.randrange(10)

	c1 =  (r1 + r2 + r3 + r4) == 21
	c2 = (r5 + r6 + r7 + r8) == 21
	c3 = (r2 == r6)

	if c1 and c2 and c3:
		print("seq1--> ", r1, r2, r3, r4)
		print("seq2--> ", r5, r6, r7, r8)
		print("*" * 30)














