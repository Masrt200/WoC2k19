# import only system from os 
import os
# import sleep to show output for some time period 
from time import sleep 
# define our clear function 
def clear():
    os.system( 'cls' )
a=input("Enter Caeser Cipher:")
#preventing garbage data type input
while True :
    try :
        b= int(input("Enter Caeser Shift:"))
        break
    except ValueError:
        print("Plz enter an integer")
        # sleep for 2 seconds after printing output then clearing
        sleep(1)
        clear()
        print("Caeser Cipher:"+a)
#func for calcing shift in cases where the limit is crossed
def julius(c) :
    d=m+int(b)%26
    if d>90+c :
        e=65+d-90-1
    elif d<65+c :
       e=90-65+d+1
    else :
        e=d
    print(chr(e),end='')
#loop for checking every char... and call julius func
for i in a :
    m=ord(i)
    if m>=65 and m<=90 :
        julius(0)
    elif m>=97 and m<=122 :
        julius(32)
    else :
        print(i,end='')
        
