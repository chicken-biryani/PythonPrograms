'''wapp to add first three integers from  following String:-
      "10 82 34 45 68" '''

data="10 82 34 45 68"

ldata = data.split(" ")
n1 = int(ldata[0])
n2 = int(ldata[1])
n3 = int(ldata[2])

res = n1 + n2 + n3
print(res)