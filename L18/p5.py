import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("petrol_prices.csv")

month = data['MONTH'].tolist()
mumbai = data['MUMBAI'].tolist()
delhi = data['DELHI'].tolist()
chennai = data['CHENNAI'].tolist()



plt.title("Petrol Price")
plt.xlabel("Months")
plt.ylabel("Prices")


plt.plot(month,mumbai,linewidth=2,marker='o',markersize=10)
plt.plot(month,delhi,linewidth=2,marker='o',markersize=10)
plt.plot(month,chennai,linewidth=2,marker='o',markersize=10)


plt.grid()
plt.savefig("price.pdf")
plt.show()