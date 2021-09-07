# wapf to find area of circle and rectangle

#python does nott support overloadind toh jugaad of default parameters
def area(p1=None, p2=None):
	if p1 is not None and p2 is None:
		ans=3.14159*p1**p2
		print("area is of circle",ans)
	elif p1 is not None and p2 is not None:
		ans = p1*p2
		print("area of rect",ans)

area(4.9)
area(2.5,6.7)