def vignere_enc(plaintext,key):
	ciphertext=''
	alphabet='abcdefghijklmnopqrstuvwxyz'

	i=0
	while i<len(plaintext):
		ct=0
		enc=plaintext[i]
		if enc.isupper():
			enc=enc.lower()
			ct+=1

		if enc in alphabet:
			encry=(ord(enc)+ord(key[i%len(key)])-194)%26

			char=chr(encry+97)
			if ct==1:
				char=char.upper()

			ciphertext+=char
		else:
			ciphertext+=enc

		i+=1

	print("Ciphertext:",ciphertext)


