#rsa encrypter
import binascii

message=input("Enter the message to be encrypted:")

byte=message.encode()
hexdump=binascii.hexlify(byte)  #used for giving hex val of binary data
print("Hex'd Message:",hexdump)

plaintext=int(hexdump,16)       #plaintext to be encrypted
print("Plain Text:",plaintext)

n=int(input("Enter the public key n:"))
if plaintext>n:
    raise Exception("Plaintext is too large for given key")
#plaintext must always be less than n...

e=int(input("Enter the public key e:"))

ciphertext=pow(plaintext,e,n)   #as per rsa encryption (c**e)%n
print("Cipher Text:",ciphertext)

input()
