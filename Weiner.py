"""weiner attack for relatively small d::
when, p<q<2p; e<n and d is of the order n**0.25
check when e is not 3 or 65537
"""
from fractions import Fraction
import math

def cont_fractions(a):
	real=a
	cont_frac=[]

	while True:
		integer=math.trunc(real)
		cont_frac.append(integer)
		fraction=real-integer
		if fraction==0:
			break
		real=1/fraction

	return cont_frac[::-1]


def approximation(e,n):
	init=Fraction(e,n)
	rev=cont_fractions(init)  #getting the reversed the array of continued fractions
	length=len(rev)
	approx=[]

	for x in range(length):
		
		try:
			frac=Fraction(1,rev[0])
		except:
			#approx.append(Fraction(0,1)) -- not appending zero since its unnecessary
			break

		j=1	
		while j<len(rev):
			cont=rev[j]+frac
			frac=1/cont
			j+=1

		rev=rev[1:] #removing first element to decrease approximation accuracy
		approx.append(1/frac)

	return approx[::-1]

def p_q(e,n):   #for returning the factors
	approx=approximation(e,n)

	m=12345
	c=pow(m,e,n) #checking d by using simple example

	for x in range(len(approx)):
		k=approx[x].numerator
		d=approx[x].denominator
		
		m0=pow(c,d,n)
		if m==m0:
			phi=(e*d-1)//k #major error occurs if we put a single '/'
			b=-1*((n-phi)+1)
			c=n
			x1=(-b+math.sqrt(b**2-4*c))/2
			x2=(-b-math.sqrt(b**2-4*c))/2
			return int(x1),int(x2),d
			break

#e=70760135995620281241019 
#n=205320043521075746592613 
def attack(e,n):
	try:
		p,q,d=p_q(e,n)
		return p,q,d,True
	except:
		print("\nWeiner Attack was unsuccessful!")
		return 0,0,0,False

	
#print(approximation())

#add condition to stop add more conditional factors if d>1/3*(n^0.25)