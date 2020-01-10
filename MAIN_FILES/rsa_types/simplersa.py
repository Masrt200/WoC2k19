#contains both simple and multi-prime rsa

import math
import binascii
import json
import requests

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
        print("\ntotient:",tot)
    elif len(factors)==1:
        print("\nfactordb failed to factorize n!")
    else:
        print("this is a multi-prime rsa!")
        print("factors:",', '.join(map(str, factors)))
        tot=1
        for x in factors:
            tot=tot*(x-1)
        print("\ntotient:",tot)

    return tot

def decrypting(m):
    print("\ndecrypted plaintext:",m)

    print("decrypted text(hex'ed out):",hex(m)[2:])

    try:
        message=binascii.unhexlify(hex(m)[2:].rstrip('L')).decode('utf-8','ignore')
    except binascii.Error:   #catching python error for odd length strings
        message=binascii.unhexlify(str('0'+hex(m)[2:].rstrip('L'))).decode('utf-8','ignore')
    except:
       print("Invalid start bytes of some places!")


    return str(message)

def init(n,e,c):

    tot=rsa_calc(n)
    d=ext_Euclid(e,tot)
    print("private key d:",d)
    m=pow(c,d,n)#using property of pow for calcing m=(c**d)%n

    return decrypting(m)
    


#try making the blocks more based on prob as the value increases
#remove i/p and o/p errors (currently prints 1 for 1,2,3,4,5,7,11,13)
#figure out extended euclidean

#padding... test-->bytes-->hex-->int of hex obtained
#reverse message obtained: int obatined-->hex-->bytes-->string
#use 3,17,65537 if nothing is given
