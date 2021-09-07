import array

a = array.array('i',[10,20,40,30,50])

print(a[:])
print(a[2:])
print(a[:3])
print(a[1:4])
print(a[2:10])
print(a[-10:2])
print(a[::])
print(a[::1])
print(a[::2])
print(a[2::2])
print(a[:10:3])
print(a[::-1])
print(a[-2:-5:-1])
print(a[::0])