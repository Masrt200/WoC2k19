#bacon cipher decryptor
ciphertext=input('Enter ciphertext:')
plaintext=''

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

value={}
y=0
for x in alphabet:
	value[y]=x
	y+=1

a=0
b=5
while True:
	while True:
		ct=0
		if a>len(ciphertext)-1:
			ct=1
			break
		elif ciphertext[a]!='a' and ciphertext[a]!='b':
			plaintext+=ciphertext[a]
		else:
			break

		a+=1
		b+=1

	if ct==1:
		break
		
	extract=ciphertext[a:b]
	extract=extract.replace('a','0')
	extract=extract.replace('b','1')
	letter_pos=int(extract,2)
	plaintext+=value[letter_pos]
	a=b
	b+=5
	if a>len(ciphertext)-1:
		break

print(plaintext)