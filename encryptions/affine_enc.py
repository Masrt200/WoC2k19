plaintext=input('Enter plaintext:')
a=int(input("Enter a(must be coprime to 26:"))
b=int(input("Enter b:"))
ciphertext=''
alphabet='abcdefghijklmnopqrstuvwxyz'

for x in plaintext:
	ct=0
	if x.isupper():
		x=x.lower()
		ct=1

	if x in alphabet:	
		pos=ord(x)-97
		cip=((a*pos)+b)%26
		char=chr(cip+97)
		if ct==1:
			char=char.upper()

		ciphertext+=char
	else:
		ciphertext+=x

print(ciphertext)
