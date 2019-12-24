import math
#import time
import binascii
import json
import requests
from small_e import root3rd
import Weiner

def factordb(n):
    url="http://factordb.com/api"
    params={"query":str(n)}
    response=requests.get(url,params=params)

    factors=response.json().get("factors")
    #output here:: ex-[['3',4],['5',3]] -- i.e., n=(3**4)*(5**3)
    fac_list = [int(x) for x,y in factors]
    #unique factors here...

    return fac_list

def ext_Euclid(A,B):  #for calcing value 'd' by extended Euclidean Algorithm
    cn=0
    if A>B:  #reversing vals in case e>totient
        A=A+B
        B=A-2*B
        A=(A-B)//2
        B=A+B
        cn+=1

    c=A   #calling vals of A and B for calcing
    d=B
    
    uc=1  #these vars are used for maintaining the 'if' condition
    vc=0
    ud=0
    vd=1

    while c!=0:
        if uc*A+vc*B==c and ud*A+vd*B==d:  #main invariant condition
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
            
    if cn==0:
        if ud<0:
            ud=B+ud
        return ud
    else:
        if vd<0:
            vd=vd+A
        return vd

def rsa_calc(n):
    factors=factordb(n)

    if len(factors)==2:
        p=factors[0]
        q=factors[1]
        print("p:"+str(p))
        print("q:"+str(q))
        tot=(p-1)*(q-1)
        print("\nTotient:",tot)
    elif len(factors)==1:
        print("\nFactordb failed to factorize n!")
    else:
        print("This is a Multi-Prime Rsa!")
        print("Factors:",factors)
        tot=1
        for x in factors:
            tot=tot*(x-1)
        print("\nTotient:",tot)

    return tot

def decrypting():
    print("\nDecrypted text:",m)

    print("\nDecrypted text(hex'ed out):"+str(hex(m)[2:]))

    try:
        message=binascii.unhexlify(hex(m)[2:].rstrip('L')).decode()
    except binascii.Error:   #catching python error for odd length strings
        message=binascii.unhexlify(str('0'+hex(m)[2:].rstrip('L'))).decode()

    print("\nDecrypted message:"+str(message))


    

"""-----------------------------
def fac(no):            #only if there was no factor db... i would have been used
    pri=math.remainder(no,6)
    if pri==1 or pri==-1 :  #checks 6n-1 and 6n+1 condition for primes
        if no%5 !=0:
            if n%no==0 :
                P[0]+=str(no)
                return 1
            
    if no==2 or no==3 or no==5:
        if n%no==0:
            P[0]+=str(no)
            return 1"""

#n=p*q, we have to factorize n for p and q
#if n is not a perfect square which it isn't since p and q are distinct primes
#it is known that p<(n)^0.5<q if p<q... which means one of the prime factors of n
#is less than its square root... also it reduces the range of search by a considerable
#amount as n increases  ~the junk algos i used in this self_made funcs


"""def check_fac(a,b):     #you can use me for one word ciphers(abt 7-8 letters)
    while a<b:
        fd=fac(a)
        if fd==1:
            return 1
            break
        a+=1"""


"""fd=0    #---->so much of code is wasted
t=0
r2=math.isqrt(n)               #square root
r3=math.floor(math.pow(n,1/3)) #cube root
r4=math.floor(math.pow(n,1/4)) #fourth root
r5=math.floor(math.pow(n,2/5)) #under root of 2.5


a=r5    #initialization
b=r2+1  #if someone if stupid enough for n=p*p
ct=1 #counts how my blocks of search have been performed(B1= r5-r2;B2= r3-r5;
#B3= r4-r3;B4= 0-r4)
while True:
    t=check_fac(a,b)
    if t==1:
        break
    
    ct+=1
    if ct==2:
        a=r3
        b=r5
    elif ct==3:
        a=r4
        b=r3
    elif ct==4:
        a=2
        b=r4
    else:
        break
-----------------------------"""
def init():
    n=int(input("Enter value of public key n:"))
    e=int(input("Enter value of public key e:"))
    C=int(input("Enter cipher text c:"))

    if e==3 and root3rd(C)<root3rd(n):
        m=root3rd(C)

    elif e<n and Weiner.attack(e,n)[3]==True: 
        p,q,d,g=Weiner.attack(e,n)
        print("\nWeiner attack was successful!")
        print("p:",p)
        print("q:",q)
        print("Private key d:",d)
        m=pow(C,d,n)
    
    else:
        print("\nFactordb was used!!")
        tot=rsa_calc()
        d=ext_Euclid(e,tot)
        print("Private key d:"+str(d))
        m=pow(C,d,n)#using property of pow for calcing m=(c**d)%n

    decrypting(m)

init()

input()
    


#try making the blocks more based on prob as the value increases
#remove i/p and o/p errors (currently prints 1 for 1,2,3,4,5,7,11,13)
#figure out extended euclidean

#padding... test-->bytes-->hex-->int of hex obtained
#reverse message obtained: int obatined-->hex-->bytes-->string
