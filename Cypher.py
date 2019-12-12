import os
from time import sleep
def clear():
    os.system('cls')

dcode=['']  #for storing the decoded word, one at a time
cy=[]       #for breaking the string into words(removing spaces)

def julius2(m,c) :  #calcing decipher'd word after shifting by 'k'
    d=m+k%26
    if d>90+c :
        e=65+d-90-1
    elif d<65+c :
       e=90-65+d+1
    else :
        e=d
    dcode[0]+=chr(e)
    
def decode(q) :        #checking whether shift to be perform'd or not, if yes
    for i in cy[q] :   #then shifting uppercase or lowercase accordingly
            m=ord(i)
            if m>=65 and m<=90 :     #if uppercase then...
                julius2(m,0)
            elif m>=97 and m<=122 :  #if lowercase then...
                julius2(m,32)
            else :                   #for spzl characters
                dcode[0]+=i

def init() :  #Entering cipher text and breaking into words
    while True :
        
        a=input("Enter Caeser Cipher:")
        if a.strip()=='' :
            print("Plz enter something")
            sleep(0.5)
            clear()
        else :
            break
        
    a=a.strip()+' '
    ed=0
    
    for i in a:    #breaking string into words
        if i==' ':
            ed=a.index(i)
            wd=a[0:ed]
            a=a[ed+1:]
            cy.append(wd)

#---------------------------------------

while True :
    b=input("Do you have the Caseser Shift(y/n):")
    f=b.casefold()
    if f=='y' or f=='n' :
        break
    print("Plz input correctly!")
    sleep(1)
    clear()

            
if f=='y' :
      import Caeser  #dont write <file_name>.py it throws back modulenotfounderror
elif f=='n' :
    
    while True :
        sleep(0.5)
        clear()
        sr=input("Do you want to perform a dictionary search(y/n):")
        S=sr.casefold()
        if S=='y' or S=='n' :
            break
        print("Plz input correctly!")
        sleep(1)
        clear()

    if S=='n' :
        init()
        k=0
        while k<=25 :
            ls=0
            print("\nShift "+str(k)+" :",end='')
            while ls<len(cy) :   
                decode(ls)   
                print(dcode[0],end=' ')
                ls+=1
                dcode[0]=''
            k+=1
            dcode[0]=''
        print("\nAll shifts are displayed!")
        
    elif S=='y' :
        print("A dictionary search for the probable solns is to be performed!!")
        init()
    
        cn=0
        k=0
        filepath='words.txt'
        while k<=25 :
            
            decode(0)  #decodes 1St word in string
            
            with open(filepath) as fp :   #access external dictionary file 
                line=fp.readline()
                while line :
                    LL=line.strip()
                    if len(LL)==len(dcode[0]) :   #matches length of word with dictnry word
                        if LL.casefold()==dcode[0].casefold() :  #matches word with dictnry word
                            print("\nPossible soln:"+ dcode[0],end=' ')
                            cn+=1
                            ls=1
                            dcode[0]=''
                            while ls<len(cy) :   #when 1st world matches all remaining follows
                                decode(ls)       #the shift of first word
                                print(dcode[0],end=' ')
                                ls+=1
                                dcode[0]=''
                            break
                    line=fp.readline()
                
            k+=1
            dcode[0]=''
        print("\nSearch Complete!")
        if cn==0 : print("Nothing was found! Sometimes BruteForce is not the best.")
    
input() #for holding output string


#adjust results so that if no.s of results are greater than 6, then the code
#looks for matching soln from the next word...
    
