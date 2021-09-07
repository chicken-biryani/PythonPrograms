#wapp for line chart depicting the petrol prices in Mumbai
#months = ["june","july","aug","sep","oct","nov","dec"]
#mumbai = [82.5,83.06,83.61,85.6,90.75,85.24,84.06]


from matplotlib import pyplot as plt

months = ["june","july","aug","sep","oct","nov","dec"]
mumbai = [82.5,83.06,83.61,85.6,90.75,85.24,84.06]

plt.plot(months,mumbai,linewidth=3,label='Mumbai',marker='o',markersize=10)
plt.xlabel("Months")
plt.ylabel("Prices")
plt.title("Petrol Prices")

plt.grid()
plt.legend()
plt.show()




































