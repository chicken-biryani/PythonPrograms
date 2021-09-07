import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("medals.csv")
print(data)

country=data['COUNTRY'].tolist()
gold_medal = data['GOLD_MEDAL'].tolist()
ex=[0.1,0,0,0]
  
plt.pie(gold_medal,labels=country,explode = ex,shadow=True,autopct='%.2f%%')

plt.show()