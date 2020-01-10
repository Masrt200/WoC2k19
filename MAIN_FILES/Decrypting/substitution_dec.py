#substituiton cipher decryptor...
import operator
from collections import deque
import os

def clear():
    os.system('cls')

def manual(ciphertext):
    _alphabet_='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    frequency={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    digraphs={'AA':0,'BB':0,'CC':0,'DD':0,'EE':0,'FF':0,'GG':0,'HH':0,'II':0,'JJ':0,'KK':0,'LL':0,'MM':0,'NN':0,'OO':0,'PP':0,'QQ':0,'RR':0,'SS':0,'TT':0,'UU':0,'VV':0,'WW':0,'XX':0,'YY':0,'ZZ':0}

    for x in ciphertext:
        if x in frequency:
            frequency[x]+=1
    x=0
    while x<len(ciphertext)-1:
        dual=ciphertext[x]
        if dual*2 in digraphs:
            if dual==ciphertext[x+1]:
                digraphs[dual*2]+=1
        
        x+=1

    sorted_f = sorted(frequency.items(), key=operator.itemgetter(1),reverse=True)
    sorted_d=  sorted(digraphs.items(), key=operator.itemgetter(1),reverse=True)

    max_steps=5
    cip_letter=deque([],maxlen=max_steps)
    plain_letter=deque([],maxlen=max_steps)

    clear()

    while True:
        print(ciphertext)
        print(sorted_f)
        print(sorted_d)
        
        cip_guess=(input('\nEnter the letter to replace,\n\'back\' to reverse last step or \'end\' to finish:')).upper()
        
        if cip_guess=='BACK':
            try:
                pos=len(plain_letter)-1
                ciphertext=ciphertext.replace(plain_letter[pos],cip_letter[pos])
                cip_letter.remove(cip_letter[pos])
                plain_letter.remove(plain_letter[pos])
            except:
                pass
        elif cip_guess=='END':
            break
        elif cip_guess in frequency or cip_guess in digraphs:
            plain_guess=(input('Enter the letter to replace with:')).lower()
            cip_letter.append(cip_guess)
            plain_letter.append(plain_guess)
            ciphertext=ciphertext.replace(cip_guess,plain_guess)
        else:
            pass
        
        clear()

    clear()
    return ciphertext
