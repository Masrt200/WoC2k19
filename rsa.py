import math
import time
import binascii

def fac(no):
    pri=math.remainder(no,6)
    if pri==1 or pri==-1 :  #checks 6n-1 and 6n+1 condition for primes
        if no%5 !=0:
            if n%no==0 :
                P[0]+=str(no)
                return 1
            
    if no==2 or no==3 or no==5:
        if n%no==0:
            P[0]+=str(no)
            return 1

def check_fac(a,b):
    while a<b:
        fd=fac(a)
        if fd==1:
            return 1
            break
        a+=1

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

P=[''] #for storing value of p        
n=int(input("Enter value of public key n:"))   #n=p*q, we have to factorize n for p and q
#if n is not a perfect square which it isn't since p and q are distinct primes
#it is known that p<(n)^0.5<q if p<q... which means one of the prime factors of n
#is less than its square root... also it reduces the range of search by a considerable
#amount as n increases

start_time=time.process_time_ns()  #for checking time efficiency

fd=0
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

p=int(P[0])
q=int(n/p)
print("p:"+str(p))
print("q:"+str(q))
tot=(p-1)*(q-1)
print("Totient:"+str(tot))

print("\nTime Taken:",end='')
print((time.process_time_ns()-start_time)/(10**9), "seconds\n")

e=int(input("Enter value of public key e:"))
d=ext_Euclid(e,tot)
print("Private key d:"+str(d))

C=int(input("Enter cipher text c:"))

m=pow(C,d,n)  #using property of pow for calcing m=(c**d)%n
print("Decrypted text:"+str(m))

message=binascii.unhexlify(hex(m)[2:]).decode()
print("Decrypted message:"+str(message))

input()
    


#try making the blocks more based on prob as the value increases
#remove i/p and o/p errors (currently prints 1 for 1,2,3,4,5,7,11,13)
#figure out extended euclidean

#padding... test-->bytes-->hex-->int of hex obtained
#reverse message obtained: int obatined-->hex-->bytes-->string
