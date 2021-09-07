#wapp for bar chart for renna and veena performance in 1st month

import numpy as np
import matplotlib.pyplot as plt

products = ["Laptop","Printer","Router"]
reena = [10,25,15]
veena = [5,30,12]
x = np.arange(len(products))

plt.bar(x , reena , width = 0.25 , label = 'Reena' , color = 'b', alpha = 0.7)
plt.bar(x+0.25 , veena , width = 0.25 , label = 'Veena' , color = 'g' , alpha = 0.7)

plt.xticks(x , products)
plt.title("Performance Analysis")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()










