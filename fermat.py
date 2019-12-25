import math

n=int(input("n:"))
a=math.floor(math.sqrt(n))

b=a**2-n
sq=0
while True:
    try:
        sq=math.sqrt(b)
    except:
        pass

    if sq!=0 and sq-int(sq)==0:
        break

    a+=1
    b=a**2-n
    
print(a-sq)
