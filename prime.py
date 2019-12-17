import math
n=int(input("Enter range:"))

Prime=[2,3]  #a no. is prime if doesnot have any multiple of prime factors
#so checking by dividing with all the prime no.s before it
i=2
while i<n:
    pri=math.remainder(i,6)
    if pri==1 or pri==-1:  #applying condition 6n-1 and 6n+1 for primes
        if i%5!=0:
            j=0
            ct=0
            while j<len(Prime):
                if Prime[j]>n/2:  #since checking for divisible primes greater than half of
                    break         #the no. is illogical
                if i%Prime[j]==0:
                    ct+=1
                j+=1
            if ct==0:
                Prime.append(i)  #appends the list of primes after each prime found
                print(i,end=' ')
    i+=1
    

    
