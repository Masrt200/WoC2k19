#railrailfence_cipher decryptor
import math

ciphertext=input("Enter cipher text:")
width=len(ciphertext)
print("Probable Solutions:")

rails=2
while rails<=width:#always >2 and <len(ciphertext)

	cycle=(rails*2)-2
	letters=math.ceil(width/cycle) #letters in the first rail

	railfence=[['' for x in range(width)] for y in range(rails)]
	gap=[cycle-x*2 for x in range(int(cycle/2))]
	plaintext=''

	j=0
	for x in range(rails):
		if x==0:
			k=0
			index=0
			while k<int(letters):
				railfence[x][index]=ciphertext[j]
				index+=gap[x]
				j+=1
				k+=1

		if x!=0:
			k=0
			index=x
			while k<int(letters):
				try:
					railfence[x][index]=ciphertext[j]
					j+=1
					railfence[x][index+gap[x]]=ciphertext[j]
					j+=1
				except:
					pass
				index+=gap[x-1]+2*x-2  #necessary adjustment
				k+=1

	pos=0
	ct=0
	x=0
	while pos<width:
	        
		plaintext+=railfence[x][pos]
		pos+=1

		if ct==0:
			x+=1
		elif ct==1:
			x-=1
		

		if x==rails-1:
			ct=1
		elif x==0:
			ct=0

	"""for x in range(rails):
		print(railfence[x])"""

	print("Solution %s:"%(rails-1)+plaintext)

	rails+=1

