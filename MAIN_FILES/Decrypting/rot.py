def rotate(sometext,skip):
	othertext=''
	alphabet='abcdefghijklmnopqrstuvwxyz'
	skip=int(skip)%26
	rot=alphabet[skip:]+alphabet[:skip]
		#for rot13, rot13='nopqrstuvwxyzabcdefghijklm'
	for x in sometext:
		ct=0
		if x.isupper():
			ct+=1
			x=x.lower()

		if x in alphabet:
			index=rot.index(x)
			add=alphabet[index]
			if ct==1:
				add=add.upper()
			othertext+=add
		else:
			othertext+=x

	return othertext
	
def rotate_brute(sometext):
	brutejunk=''
	i=1
	while i<26:
		plaintext=''
		plaintext=rotate(sometext,i)

		brutejunk+='ROT %s: ' % i+plaintext+'\n'
		i+=1

	return brutejunk







	