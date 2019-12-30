#railfence encryptor
import math

plaintext=input('Enter plain text:')
rails=int(input('Enter no. of rails:'))#always >2 and <len(ciphertext)
width=len(plaintext) 

railfence=[['' for x in range(width)] for y in range(rails)]

x=0
pos=0
ct=0
while pos<width:
        
	railfence[x][pos]=plaintext[pos]
	pos+=1

	if ct==0:
		x+=1
	elif ct==1:
		x-=1
	

	if x==rails-1:
		ct=1
	elif x==0:
		ct=0 

ciphertext=''
for x in range(rails):
	for y in range(width):
		if railfence[x][y]!='':
			ciphertext+=railfence[x][y]
for x in range(rails):
	print(railfence[x])

print(ciphertext)



