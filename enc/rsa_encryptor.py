#rsa encrypter
import binascii

def rivest(n,e,message):
	byte=message.encode()
	hexdump=binascii.hexlify(byte)  #used for giving hex val of binary data
	print("hex'd message:",hexdump)

	plaintext=int(hexdump,16)       #plaintext to be encrypted
	print("plain text:",plaintext)

	#n=int(input("enter public key n:"))
	if plaintext>n:
	    raise Exception("plaintext is too large for given key")
	#plaintext must always be less than n...

	#e=int(input("enter public key e:"))

	ciphertext=pow(plaintext,e,n)   #as per rsa encryption (c**e)%n

	return ciphertext