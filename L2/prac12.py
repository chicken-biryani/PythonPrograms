#Wapp to read two range r1 & r2 from user
# If num is multiple of 3-o/p: SS
#                             of 5-o/p: NCp
#                             of 3 & 5 -op:cong
#r1=7  & r2=20
# 9-SS  15-Cong
# 10-NCP  18-SS
#12-SS 20-NCP
r1 = int(input("Enter lower range "))
r2 = int(input("Enter higher range "))

if r1 > r2:
	r1,r2 = r2,r1

for i in range(r1,r2+1):
	if ((i%3==0)  and (i%5==0)):
		print(i, "-Cong",sep='')
	elif (i%3==0):
		print(i, "-Ss",sep='')
	elif (i%5==0 ):
		print(i,"-Ncp",sep='')







