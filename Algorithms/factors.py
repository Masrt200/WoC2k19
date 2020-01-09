import requests
import json

#n=int(input("Enter public key n:"))
def factordb(n):

	url="http://factordb.com/api"
	params={"query":str(n)}
	response=requests.get(url,params=params)

	factors=response.json().get("factors")
	#output here::[['3',4],['5',3]] -- i.e., n=(3**4)*(5**3)
	fac_list = [int(x) for x,y in factors]
	#prints unique factors here...
	print(fac_list)
	#print(response.json())

factordb(252)

