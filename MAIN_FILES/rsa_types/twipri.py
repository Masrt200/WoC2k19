"""twin prime case in rsa
q=p+2
n=p(p+2)--> n=p^2+2p--> p^2+2p-n=0 simple quadrartic
a=1, b=2, c=-n"""
import math

def pri(n):
	D=math.sqrt(n+1)

	p=D-1

	return p, int(n/p)
