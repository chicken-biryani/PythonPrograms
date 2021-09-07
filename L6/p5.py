# wamdpp to billing amount gen...

menu = {"upma":20,"idli":30,"vada":20}
amount = 0.0
while True:
	op = int(input("1 add item, 2 amount and 3 exit "))
	if op == 1:
		name = input("Enter food item name ")
		price = menu.get(name,0)
		if price == 0:
			print("invalid food item name")
		else:
			qty = int(input("Enter the quantity "))
			amount = amount + price * qty
	elif op == 2:
		print("Amount = ",amount)
	elif op == 3:
		break
	else:
		print("Invalid option")