#wapp to read csv file and draw a bar chart for job demand in 2017 and 2018

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("jobs.csv")
language = data['LANGUAGE'].tolist()
jobs_2017 = data['JOBS_2017'].tolist()
jobs_2018 = data['JOBS_2018'].tolist()

x = np.arange(len(language))

plt.bar(x , jobs_2017 , width = 0.25 , label = '2017')
plt.bar(x+0.25 , jobs_2018 , width = 0.25 , label = '2018')

plt.xticks(x ,language)
plt.title("Job Demand")
plt.xlabel("Languages")
plt.ylabel("Jobs")
plt.legend()
plt.grid()
plt.show()








