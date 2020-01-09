ciphertext=input('Enter cipher text:')
plaintext=''
alphabet='abcdefghijklmnopqrstuvwxyz'
atbash='zyxwvutsrqponmlkjihgfedcba'
#for rot13, rot13='nopqrstuvwxyzabcdefghijklm'
for x in ciphertext:
	ct=0
	if x.isupper():
		ct+=1
		x.lower()

	if x in alphabet:
		index=atbash.index(x)
		add=alphabet[index]
		if ct==1:
			add=add.upper()
		plaintext+=add
	else:
		plaintext+=x

print(plaintext)

