import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("petrol_prices.csv")
#print(data)

month = data['MONTH'].tolist()
mumbai = data['MUMBAI'].tolist()
delhi = data['DELHI'].tolist()
chennai = data['CHENNAI'].tolist()

#print(month)
#print(mumbai)
#print(delhi)
#print(chennai)

plt.plot(month,mumbai,label='Mumbai', markersize=5 , marker='o')
plt.plot(month,delhi,label='Delhi', markersize=5 , marker='o')
plt.plot(month,chennai,label='Chennai', markersize=5 , marker='o')
plt.xlabel("Months")
plt.ylabel("Prices")
plt.title("Petrol Prices")
plt.grid()
plt.legend()
plt.show()