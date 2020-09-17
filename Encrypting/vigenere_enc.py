def encrypt(plaintext,key):
	key=key.lower()
	ciphertext=''
	alphabet='abcdefghijklmnopqrstuvwxyz'

	plaintext_adj=''

	for i in plaintext:
		if i.lower() in alphabet:
			plaintext_adj+=i


	i=0
	j=0
	while j<len(plaintext):
		enc=plaintext[j]

		if enc in plaintext_adj:
			ct=0
			
			if enc.isupper():
				enc=enc.lower()
				ct+=1

			
			encry=(ord(enc)+ord(key[i%len(key)])-194)%26

			char=chr(encry+97)
			if ct==1:
				char=char.upper()

			ciphertext+=char

			i+=1

		else:
			ciphertext+=enc

		j+=1
		

	print(ciphertext)

encrypt('Wzhu{ufsifx_xmtzqi_sty_gk_uzy_ns_ujsx}','CUTENESS')


