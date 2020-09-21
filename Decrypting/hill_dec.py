from sympy import *
import math

def jill(ciphertext,key):
	ciphertext,key=ciphertext.upper(),key.upper()
	plaintext=''
	
	CIPV=[ord(i)-65 for i in ciphertext]
	KEYV=[]

	lim=int(math.sqrt(len(key)))

	for i in range(lim):
		row=[]
		for j in range(lim):
			row.append(ord(key[lim*i+j])-65)
		KEYV.append(row)


	KEYV=[[1.6,-1.4,1.8],[2.2,-1.8,1.6],[-1,1,-1]]
	CIPV=Matrix(CIPV)
	KEYV=Matrix(KEYV)

	det=KEYV.det()%26
	IKEYV=(det*KEYV.adjugate())%26

	print(IKEYV)
	PLNV=(IKEYV*CIPV)%26

	for i in PLNV:
		plaintext+=chr(i+65)

	return plaintext

print(jill('SWK','HILLMAGIC'))