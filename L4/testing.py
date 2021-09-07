s1="vishal"
s2="Vishala"
s3="      vimal      okkkay    "
s4="i LovE MilO"
print(s1==s2)    #checks their elements i.e unicode of every letter is compared
print(s1 is s2)  #checks address
print(hex(id(s1)))
print(hex(id(s2)))  #would give address 
print(len(s1))
print(s3.count(' '))
print(s1.replace('a','e'))

print(s3.lstrip())
print(s3.rstrip())
print(s3.strip())
print(s4.title())
print(s4.swapcase())
print(s4.find('i'))
print(s4.index('i'))
print(s4.rfind('i'))
print(s4.capitalize())
print(s4.lower())
print(s4.upper())
print(s4.isdigit())
a=s1.split('')
print(a)
