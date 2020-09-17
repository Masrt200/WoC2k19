import os

location=str(os.getcwdb())[2:-1]

try:
	os.mkdir('D:\\crrypic')
except:
	pass

f1=open('D:\\crrypic\\path.txt','w')
f1.write(location)
f1.close()

