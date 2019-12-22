#extended Euclid

a=int(input("Enter 1st no.:"))
b=int(input("Enter 2nd no.:"))
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


print(str(ud)+"*"+str(a)+"+"+str(vd)+"*"+str(b)+"="+str(d))

if ud<0:
    print(b+ud)
