import operator

def impossible(ciphertext,length):
	real_cipher=ciphertext

	ciphertext=ciphertext.lower()
	alphabet='abcdefghijklmnopqrstuvwxyz'

	ciphertext_adj=''

	for i in ciphertext:
		if i in alphabet:
			ciphertext_adj+=i

	key=2
	key_max=10
	if length!=None:
		key_max=int(length)
	key_blocks=[]
	index_of_coincidence={}
	true_key=''
	arr_key=[]
	plaintext=''

	while key<=key_max:
		blocks=[]
		i=0
		while i<key:
			blocks.append(ciphertext_adj[i::key])
			i+=1

		key_blocks.append(blocks)
		key+=1

	for x in key_blocks:
		avg=0
		for y in x:
			count={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
			ic=0
			n=0
			for z in y:
				if z in count:
					count[z]+=1
					n+=1

			for z in alphabet:
				ic+=count[z]*(count[z]-1)
			
			ic=ic/(n*(n-1))
			avg+=ic

		avg=avg/len(x)
		index_of_coincidence[len(x)]=avg


	index_of_coincidence = sorted(index_of_coincidence.items(), key=operator.itemgetter(1),reverse=True)
	index=index_of_coincidence[0][0]
	true_key_block=key_blocks[index-2]

	for x in true_key_block:
		probabilty={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0}
		i=0
		while i<26:
			plain=''
			frequency={'e':12.702,'t':9.356,'a':8.167,'o':7.507,'i':6.966,'n':6.749,'s':6.327,'r':5.987,'h':6.094,'d':4.253,'l':4.025,'u':2.758,'c':2.202,'m':2.406,'f':2.228,'y':1.994,'w':2.560,'g':2.015,'p':1.929,'b':1.492,'v':0.978,'k':1.292,'x':0.150,'q':0.095,'j':0.153,'z':0.077}
			for z in x:
				if z in alphabet:
					y=ord(z)-i%26
					if y>122:
						y=y-26
					elif y<90:
						y=y+26
					plain+=chr(y)
				else:
					plain+=z

			total=0
			count={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
			for y in plain:
				if y in alphabet:
					count[y]+=1
					total+=1

			for w in frequency:
				frequency[w]=(frequency[w]*total)/100

			chi_sq=0
			for q in alphabet:
				try:
					squared=((count[q]-frequency[q])**2)/frequency[q]
					chi_sq+=squared
				except:
					chi_sq=0

			probabilty[i]=chi_sq

			i+=1
			#print(chi_sq)

		probabilty=sorted(probabilty.items(), key=operator.itemgetter(1))
		#print(probabilty)
		for x in range(len(probabilty)):
			if probabilty[x][1]!=0:
				arr_key.append(chr(probabilty[x][0]+97))
				break

	true_key=''.join(arr_key)

	print("key:",true_key)

	check=input("do you want to change the key(y/n):")

	if check=='y':
		pos=int(input("enter position of character:"))
		char=input("enter character to replace:")
		arr_key[pos]=char
	else:
		pass

	true_key=''.join(arr_key)
	print('final Key:',true_key)

	plaintext=withkey(real_cipher,true_key)

	return plaintext.encode('utf-8') #for preventing unicode error  


def withkey(ciphertext,true_key):
	true_key=true_key.lower()
	plaintext=''

	alphabet='abcdefghijklmnopqrstuvwxyz'
	ciphertext_adj=''

	for i in ciphertext:
		if i.lower() in alphabet:
			ciphertext_adj+=i

	
	i=0
	j=0
	while j<len(ciphertext):
		enc=ciphertext[j]
		if enc in ciphertext_adj:
			ct=0

			if enc.isupper():
				enc=enc.lower()
				ct=1
			
			decry=(ord(enc)-ord(true_key[i%len(true_key)]))%26
			char=chr(decry+97)

			if ct==1:
				char=char.upper()

			plaintext+=char
			i+=1

		else:
			plaintext+=enc

		j+=1

	return plaintext

#can also use chcp 65001 in the terminal in case of unicode error















#print(len(true_key_block))


#print(index_of_coincidence)



