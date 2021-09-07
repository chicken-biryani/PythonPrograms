#create a package mypack2 with a module myconventer with two functions
#1. ssv to csv :- i/p- kamal rocks -> kamal,rocks
#2.csv to ssv :- i/p- kamal,rocks -> kamal rocks

def ssvtocsv(s):
	data = s.split(" ")
	ndata = ','.join(data)
	return ndata

def csvtossv(s):
	data = s.split(",")
	ndata = ' '.join(data)
	return ndata