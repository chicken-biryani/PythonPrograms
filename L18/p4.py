import matplotlib.pyplot as plt

months=['june','july','aug','sep','oct','nov','dec']
mumbai=[82.5,83.06,83.61,85.6,90.75,85.24,84.06]

plt.title("Petrol Prices")
plt.xlabel("Months")
plt.ylabel("Prices")

plt.plot(months,mumbai,linewidth=3,marker='o',markersize=10,label='Mumbai')

plt.legend()
plt.grid()
plt.savefig("mum_price.pdf")
plt.show()