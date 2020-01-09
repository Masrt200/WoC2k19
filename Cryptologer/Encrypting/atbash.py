def atb(sometext):
	othertext=''
	alphabet='abcdefghijklmnopqrstuvwxyz'
	atbash='zyxwvutsrqponmlkjihgfedcba'
	#for rot13, rot13='nopqrstuvwxyzabcdefghijklm'
	for x in sometext:
		ct=0
		if x.isupper():
			ct+=1
			x.lower()

		if x in alphabet:
			index=atbash.index(x)
			add=alphabet[index]
			if ct==1:
				add=add.upper()
			othertext+=add
		else:
			othertext+=x

	return othertext

