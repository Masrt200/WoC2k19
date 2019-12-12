import os
from time import sleep
def clear():
    os.system('cls')

while True:
    td=input("What to do encrypt/decrypt?(e/d):")
    Td=td.casefold()
    if Td=='d' :
        a=input("Enter Vigenere Cipher:")
        break
    elif Td=='e' :
        a=input("Enter Plain Text:")
        break
    else :
        print("Plz input correctly!")
        sleep(1)
        clear()
    
Cy=list(a)
Dy=[]

while True :   #checking for key format
    b=input("Enter Key:")
    Ky=list(b)
    k=0
    while k<len(Ky) :
        p=ord(Ky[k])
        if p>=65 and p<=90 :
            pass
        elif p>=97 and p<=122 :
            pass
        else :
            print("The key should contain only letters")
            sleep(1)
            clear()
            break
        k+=1

    if k==len(Ky) :
        break

def decipher(c,j,kl) :
    d=(ord(Cy[j])-kl)%26 #character code for decrypted letter
    Dy.append(chr(d+c))

def encipher(c,j,kl) :
    d=(ord(Cy[j])+kl-2*c)%26 #character code for encrypted letter
    Dy.append(chr(d+c))

if Td=='e' :
    func=encipher
elif Td=='d' :
    func=decipher


i=0
while i<len(Cy) :  #Finding the encr or decr text
    m=ord(Cy[i])
    lk=ord(Ky[i%len(Ky)])
    if m>=65 and m<=90 :
        
        if Ky[i%len(Ky)].islower()==True : #for converting lower case letters in  key to match with upper case ones
            lk=lk-32
            
        func(65,i,lk)
    elif m>=97 and m<=122 :
        
        if Ky[i%len(Ky)].isupper()==True : #vice-versa
            lk=lk+32
            
        func(97,i,lk)
    else :
        Dy.append(Cy[i])
    i+=1

b=''
if Td=='e' :
    print("Encrypted Cipher:"+b.join(Dy))
elif Td=='d' :
    print("Decrypted Soln:"+b.join(Dy))

input()


    
    
        
