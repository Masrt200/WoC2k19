#Euclid~ algorithm for finding the gcd of two no.s
        
def Euclid(a,b):
    m=a
    n=b
    if a>b:
        m=b
        n=a

    r=m%n
    r1=n
    while r!=0 :
        r2=r1%r
        r1=r
        r=r2
    return r1


def init():
    a=int(input("Enter 1st no:"))
    b=int(input("Enter 2nd no:"))
    gcd=Euclid(a,b)
    print("GCD of "+str(a)+" and "+str(b)+" is:"+str(gcd))

init()
