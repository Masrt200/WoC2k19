"""import only system from os 
import os
# import sleep to show output for some time period 
from time import sleep 
# define our clear function 
def clear():
    os.system( 'cls' )"""

def julius(ciphertext,shift):
	alphabet='abcdefghijklmnopqrstuvwxyz'
	plaintext=''
	for x in ciphertext:
		ct=0
		y=0
		if x.isupper():
			x=x.lower()
			ct=1

		if x in alphabet:
			y=ord(x)+shift%26
			if y>122:
				y=y-26
			elif y<90:
				y=y+26
			letter=chr(y)
			if ct==1:
				letter=letter.upper()

			plaintext+=letter
		else:
			plaintext+=x

	return plaintext

def bruteforce(ciphertext):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    i=0
    brutejunk=''
    while i<26:
        plaintext=''
        for x in ciphertext:
            ct=0
            if x.isupper():
                x=x.lower()
                ct=1

            if x in alphabet:
                y=(ord(x)-97+i)%26

                char=chr(y+97)
                if ct==1:
                    char=char.upper()

                plaintext+=char
            else:
                plaintext+=x

        brutejunk+='shift %s: ' % i+plaintext+'\n'

        i+=1

    return brutejunk



        
