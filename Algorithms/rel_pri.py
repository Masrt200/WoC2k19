#prog for calcing all no.s relatively prime to the totient

def Euclid(a,b):  #calcing gcd didnt feel like using math func
    m=a
    n=b

    r=m%n
    r1=n
    while r!=0 :
        r2=r1%r
        r1=r
        r=r2

    return r1

tot=int(input("Enter the Totient:"))
E=[]


i=1
while i<tot:
     check=Euclid(tot,i)

     if check==1:
         E.append(i)

     i+=1
     
print(E)

input()
#add random
