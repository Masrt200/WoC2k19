'''
for cases where cipher text is broken into various RSA encrypted messages
c must be an array of those ciphers
'''
import json
from simplersa import rsa_calc
from sympy import mod_inverse

def multi(n,e,c):
	tot=rsa_calc(n)
	d=mod_inverse(e,tot)
	c=json.loads(c)
	m=[]
	for i in c:
		m.append(i,d,n)

	return m
		

