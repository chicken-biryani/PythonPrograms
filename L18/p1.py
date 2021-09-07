import matplotlib.pyplot as plt 

products = ["parle",'marie','monaco']

dmart=[4.80,9.8,8.5]

plt.bar(products,dmart,color='g')

plt.xlabel('names')

plt.ylabel('prices')

plt.title("biscuits")

plt.grid()
plt.show()