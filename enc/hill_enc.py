import math
from sympy import *

def jack(plaintext,key):
	plaintext,key=plaintext.upper(),key.upper()
	ciphertext=''
	
	MESV=[ord(i)-65 for i in plaintext]
	KEYV=[]

	lim=int(math.sqrt(len(key)))

	for i in range(lim):
		row=[]
		for j in range(lim):
			row.append(ord(key[lim*i+j])-65)
		KEYV.append(row)

	MESV=Matrix(MESV)
	KEYV=Matrix(KEYV)

	CIPV=(KEYV*MESV)%26
	
	for i in CIPV:
		ciphertext+=chr(i+65)

	return ciphertext	

#original-->
message='MAN'
key='HILLMAGIC'

print(jack(message,key))

#IKEYV=(det*KEYV.adjugate())%26
#det=KEYV.det()%26
#PLNV=(IKEYV*CIPV)%26