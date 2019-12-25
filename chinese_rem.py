#chinese remainder theorem
import binascii

def root3rd(x):
    y, y1 = None, 2
    while y!=y1:
        y = y1
        y3 = y**3
        d = (2*y3+x)
        y1 = (y*(y3+2*x)+d//2)//d
    return y

def Euclid(a,b):
    if a>b:   #reversing values of a and b
        a=a+b
        b=a-2*b
        a=(a-b)//2
        b=a+b

    c=a   #calling vals of a and c for calcing
    d=b

    uc=1  #these vars are used for maintaining the 'if' condition
    vc=0
    ud=0
    vd=1

    while c!=0:
        if uc*a+vc*b==c and ud*a+vd*b==d:  #main invariant condition
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

    #if ud<0:
    #   ud=ud+b

    return ud

def init():
    e=int(input("Enter no. of ciphers captured:"))
    n=[]
    N=[]
    c=[]
    a=[]
    M=0
    Num=1
    for x in range(e):
        moduli=int(input("n"+str(x+1)+":"))
        div=int(input("c"+str(x+1)+":"))
        c.append(div)
        n.append(moduli)
        Num=Num*moduli

    for x in range(e):
        y=x+1
        if y==e: y=0
        div=n[x]*n[y]
        N.append(div)

    for x in range(e):
        rem=Euclid(N[x],n[x])
        a.append(rem)

    for x in range(e):
        M+=(c[x]*N[x]*a[x])%Num

    #M=M%Num

    m=root3rd(M)
    print(m,M)
    print((binascii.unhexlify(hex(m)[2:])).decode())

init()
