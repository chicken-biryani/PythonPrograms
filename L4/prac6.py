


for i in range(100,1000):
	sum=0
	num=i
	orignal=num	
	while(num>0):
		digit=num%10
		sum=sum+digit**3
		num=num//10
	if(orignal==sum):
		print(orignal)
	


