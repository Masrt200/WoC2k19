plaintext=input('Enter plaintext:').upper()

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
value={}

y=0
for x in alphabet:
	value[x]=y
	y+=1

ciphertext=''
for x in plaintext:
	ct=0
	if x in alphabet:
		binary=bin(value[x])[2:]
		if len(binary)<5:
			binary='0'*(5-len(binary))+binary

		binary=binary.replace('0','a')
		binary=binary.replace('1','b')
		ciphertext+=binary
	else:
		ciphertext+=x

print(ciphertext)
