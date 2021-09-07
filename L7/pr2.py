def check(num):
	org_num = num
	sum = 0
	while num!=0:
		digit =num%10
		sum = sum+ digit**3
		num =num//10
	if org_num == sum:
		return True
	else:
		return False
for num in range(100,1000):
	if check(num):
		print(num)











