'''data "a,2 b,4 c,3"
o/p- a a
        b b b b
        c c c '''
data = "a,2,b,4,c,3"

ldata = data.split(",")
for i in range(0,len(ldata),2):
	what = ldata[i]
	how = int(ldata[i+1])
	print((what + "\t") * how ,end = ' ')
	print( )
