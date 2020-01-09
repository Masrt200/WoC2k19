import operator
#from sympy import mod_inverse
def Euclid(a,b):

    c=a   #calling vals of a and c for calcing
    d=b

    uc=1  #these vars are used for maintaining the 'if' condition
    vc=0
    ud=0
    vd=1

    while c!=0:
        if uc*a+vc*b==c and ud*a+vd*b==d:  #main invariant condition
            q=d//c
            m=c  #storing c
            c=d-q*c
            d=m
        
            Uc=uc #storing uc and vc
            Vc=vc
        
            uc=ud-q*uc
            vc=vd-q*vc
            ud=Uc
            vd=Vc

    if ud<0:
    	ud=ud+b
        
    return ud




ciphertext=input("Enter ciphertext:")
#e=(ax+b)%26
alphabet='abcdefghijklmnopqrstuvwxyz'

frequency={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
stats=['e','t','a','o','i','n','s']
index=[]
AB=[]
plaintext=''

for x in ciphertext:
	a=x.lower()
	if a in frequency:
		frequency[a]+=1

sorted_f = sorted(frequency.items(), key=operator.itemgetter(1),reverse=True)

for x in range(len(stats)):
	i=0
	while i<x:
		index.append((i,x))
		index.append((x,i))
		i+=1

A=0
B=0
for y in index:
	ct=0
	initials=[sorted_f[0][0],stats[y[0]]],[sorted_f[1][0],stats[y[1]]]

	a=[3,5,7,9,11,15,17,19,21,23,25]
	for x in a:
		b=0
		while b<26:
			e=((x*(ord(initials[0][1])-97))+b)%26
			if e==ord(initials[0][0])-97:
				break
			b+=1

		e2=((x*(ord(initials[1][1])-97))+b)%26
		if e2==ord(initials[1][0])-97:
			AB.append([x,b])
			break

for y in AB:
	A=y[0]
	B=y[1]
	Ainv=Euclid(A,26)
	for x in ciphertext:
		ct=0
		if x.isupper():
			x=x.lower()
			ct=1

		if x in alphabet:
			pos=ord(x)-97
			z=(Ainv*(pos-B))%26
			char=chr(z+97)
			if ct==1:
				char=char.upper()

			plaintext+=char
		else:
			plaintext+=x

	print(plaintext,'\n')
	plaintext=''




	





