#Euclid~ algorithm for finding the gcd of two no.s

a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))

m=a
n=b
if b>a :
    m=b
    n=a

r=m%n
r1=n
while r!=0 :
    r2=r1%r
    r1=r
    r=r2

print("GCD of "+str(m)+" and "+str(n)+" is:"+str(r1))

input()
