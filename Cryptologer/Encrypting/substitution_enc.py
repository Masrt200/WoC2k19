#substitution cipher encryptor...

def substitute(plaintext):
    plaintext=plaintext.upper()
    _alphabet_='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _alphabet_new_=''

    keyword=input('Enter Keyword:')
    keyword=(keyword.strip()).upper()
    key_list=[]
    for x in keyword:
        ct=1
        for y in key_list:
            if x==y:
                ct=0
                break
        if ct==1:
            key_list.append(x)
            
    _alphabet_new_=''.join(key_list)

    for x in _alphabet_:
    	ct=1
    	for y in key_list:
    		if x==y:
    			ct=0
    			break
    	if ct==1:
    		_alphabet_new_+=x

    print(_alphabet_+'\n'+_alphabet_new_)

    ciphertext=''

    for x in plaintext:
        ct=0
        for y in _alphabet_:
            if x==y:
                pos=_alphabet_.index(y)
                ciphertext+=_alphabet_new_[pos]
                ct=1
        
        if ct==0:
            ciphertext+=x

    return ciphertext
