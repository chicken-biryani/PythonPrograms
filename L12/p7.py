import pandas as pd

data = pd.read_csv("student.csv")
#print(data)
#print(data.shape)
#print(data.head())
#print(data.head(3))
#print(data.tail())
#print(data.tail(3))
#print(data[2:5])
#print(data[1:7:2])
#print(data[data['LOCATION'] == 'THANE' ])

'''thane =data[data['LOCATION'] == 'THANE' ]
thane.to_csv("thane.csv") '''

#print(data.sort_values(by = 'NAME'))
#print(data.sort_values(by = 'NAME',ascending=0))

'''ndata = data.sort_values(by='SEM1',ascending=0)
print(ndata.head(1))'''

'''ndata = data.sort_values(by='SEM1',ascending=0)
print(ndata[1:2])'''

'''ndata = data[data['NAME'].str.startswith("S")]
print(ndata)'''

'''ndata = data[data['SEM2'] > 80]
print(ndata)'''

ndata = data[ (data['SEM1'] < 80) & (data['LOCATION'] == 'THANE') ]
print(ndata)


























