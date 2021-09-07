import matplotlib.pyplot as plt 
import numpy as np
products = ["parle",'marie','monaco']

dmart=[4.80,9.8,8.5]
bigb=[5,6,10]
x=np.arange(len(products)) #arange give  floating point 
plt.bar(x,dmart,color='g',width=0.25,label='Dmart')
plt.bar(x+0.25,bigbazar,color='r',width='r',width=0.25)

plt.xlabel('names')

plt.ylabel('prices')

plt.title("biscuits")

plt.grid()
plt.show()