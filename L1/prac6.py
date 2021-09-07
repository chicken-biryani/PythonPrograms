#wapp to read temp in cel and convert to fah

cel=float(input("Enter temp in cel "))
fah = cel*1.8+32
print("cel = ",cel, "\u00B0", "fah = ",fah, "F")
print("cel = %.2f\u00B0  fah = %.2fF" %(cel,fah))
