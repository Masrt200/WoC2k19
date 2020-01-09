#simple polybius square encryption,
def tsquaree(plaintext):
	plaintext=plaintext.lower()
	alphabet='abcdefghijklmnopqrstuvwxyz'

	square=[['a','b','c','d','e','f'],['g','h','i','j','k','l'],['m','n','o','p','q','r'],['s','t','u','v','w','x'],['y','z','0','1','2','3'],['4','5','6','7','8','9']]
	ciphertext=''

	for x in plaintext:
		if x in alphabet:
			b=0
			while b<6:
				if x in square[b]:
					ciphertext+=str(b+1)+str(square[b].index(x)+1)
				b+=1
		else:
			ciphertext+=x


	return ciphertext