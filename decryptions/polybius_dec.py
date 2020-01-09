ciphertext=input('Enter ciphertext:')
number='0123456789'
square=[['a','b','c','d','e','f'],['g','h','i','j','k','l'],['m','n','o','p','q','r'],['s','t','u','v','w','x'],['y','z','0','1','2','3'],['4','5','6','7','8','9']]
plaintext=''

x=0
while x<len(ciphertext):
	if ciphertext[x] in number:
		X=int(ciphertext[x])-1
		Y=int(ciphertext[x+1])-1

		plaintext+=square[X][Y]
		x+=2
	else:
		plaintext+=ciphertext[x]
		x+=1

print(plaintext)
