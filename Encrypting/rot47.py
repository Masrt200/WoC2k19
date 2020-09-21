def rot47(sometext):
	
	othertext=''
	charset=[]	

	for i in range(33,127):
		charset.append(chr(i))

	ROTset=charset[47:]+charset[:47]

	for i in sometext:
		if i in charset:
			othertext+=ROTset[charset.index(i)]
		else:
			othertext+=i

	return othertext



