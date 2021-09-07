import pandas as pd
import matplotlib.py as plt

sdata=pd.read_csv("student_scor.csv")
print(sdata)

mumstu=sdata[sdata.LOCATION=="MUMBAI"]

print(mumstu)

name=mumstu['NAME'].tolist()
sem1=mumstu['SEM1'].tolist()

print(name)
print(sem1)
plt.bar(name,sem1)
plt.show()