#extended Euclid
import binascii
import math

def Euclid_RSA(a,b):

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


def reversing(n,d,c):
    m=pow(c,d,n)
    return printing(m)

def printing(m):
    
    print("\ndecrypted plaintext:",m)
    print("decrypted text(hex'ed out):",hex(m)[2:])

    try:
        message=binascii.unhexlify(hex(m)[2:].rstrip('L')).decode('utf-8','ignore') #ignoring improper bytes
    except binascii.Error:   #catching python error for odd length strings
        message=binascii.unhexlify(str('0'+hex(m)[2:].rstrip('L'))).decode('utf-8','ignore')


    return str(message)