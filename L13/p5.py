#wapp to read data from csv files about country name and gold medals and create a pie chart

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("medals.csv")
country = data['COUNTRY']
gold_medal = data['GOLD_MEDAL'].tolist()
plt.pie(gold_medal , labels = country, radius=1.3, explode = [0.1,0,0,0] , shadow = True , autopct='%.2f%%')
plt.axis("equal")
plt.show()