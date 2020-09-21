

# This file was *autogenerated* from the file franklin.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_30 = Integer(30); _sage_const_8 = Integer(8); _sage_const_2 = Integer(2); _sage_const_25 = Integer(25); _sage_const_16 = Integer(16); _sage_const_3 = Integer(3); _sage_const_8192 = Integer(8192); _sage_const_400 = Integer(400); _sage_const_512 = Integer(512); _sage_const_11 = Integer(11); _sage_const_17370303838481078396867008243308868112257548548059095304083176419843329544293059453520977785834201881316544058052761790042480195917382530503087478512154073955285051612704957561001426537455932438432825389315081737200485166417839753998573473081451603834791415253334463365998854998601877157916654540843809424104242227923498742916025820673577009094160761889056257135441612310708909004386515228803850326325845220127547339982229710596800585045146371251910429634814493586813571760891089473908424811524178069610620015296633934386201883491772987354038148907269759119662847942525255096401374349773830992807068488771538369615601 = Integer(17370303838481078396867008243308868112257548548059095304083176419843329544293059453520977785834201881316544058052761790042480195917382530503087478512154073955285051612704957561001426537455932438432825389315081737200485166417839753998573473081451603834791415253334463365998854998601877157916654540843809424104242227923498742916025820673577009094160761889056257135441612310708909004386515228803850326325845220127547339982229710596800585045146371251910429634814493586813571760891089473908424811524178069610620015296633934386201883491772987354038148907269759119662847942525255096401374349773830992807068488771538369615601); _sage_const_16646831158806362802187786053000847261352801407099627746656981114264123084291482087935961192670001789636361880742010535618183534314220263031070941144065110371402447505746517004758102622790324243066396378400917586946919353139062614850945782319128404685532864981377048244949294554932057980152355001919018067262729763614490719982533034554246049279851204024827156143138168212490307695216862836737368783077055248476317242183876942418147147304741277868711942793107820496026090839674446132795424932123971125810013756582530141492598683805356372579158966224469542526376498536480134410937637687299998645887813353420966692508791 = Integer(16646831158806362802187786053000847261352801407099627746656981114264123084291482087935961192670001789636361880742010535618183534314220263031070941144065110371402447505746517004758102622790324243066396378400917586946919353139062614850945782319128404685532864981377048244949294554932057980152355001919018067262729763614490719982533034554246049279851204024827156143138168212490307695216862836737368783077055248476317242183876942418147147304741277868711942793107820496026090839674446132795424932123971125810013756582530141492598683805356372579158966224469542526376498536480134410937637687299998645887813353420966692508791); _sage_const_16642663284727388869359397895910335272404595771284103150936358833231470509861640332583361340545124075244886609346899258782739975148997172295074570753127729508759434428381195625867385590828103084995319972798272253634439508974882475880556987849817425770370990761372886789636999323951617453484184957925135433933493595337090091421803222839756611595987594830775847945534456242467806653835522509335138058889714784179670869987360131362472966955922431532692142416069620336546710451989259697070802523963315535188681552814176454454076107504282177864254923316731884568894436596459435508067440009534686683478813445176905136545485 = Integer(16642663284727388869359397895910335272404595771284103150936358833231470509861640332583361340545124075244886609346899258782739975148997172295074570753127729508759434428381195625867385590828103084995319972798272253634439508974882475880556987849817425770370990761372886789636999323951617453484184957925135433933493595337090091421803222839756611595987594830775847945534456242467806653835522509335138058889714784179670869987360131362472966955922431532692142416069620336546710451989259697070802523963315535188681552814176454454076107504282177864254923316731884568894436596459435508067440009534686683478813445176905136545485)# Franklin-Reiter attack against RSA.
# If two messages differ only by a known fixed difference between the two messages
# and are RSA encrypted under the same RSA modulus N
# then it is possible to recover both of them.

# Inputs are modulus, known difference, ciphertext 1, ciphertext2.
# Ciphertext 1 corresponds to smaller of the two plaintexts. (The one without the fixed difference added to it)
def franklinReiter(n,e,r,c1,c2):
    R = Zmod(n)['X']; (X,) = R._first_ngens(1)
    f1 = X**e - c1
    f2 = (X + r)**e - c2
    # coefficient 0 = -m, which is what we wanted!
    return Integer(n-(compositeModulusGCD(f1,f2)).coefficients()[_sage_const_0 ])

  # GCD is not implemented for rings over composite modulus in Sage
  # so we do our own implementation. Its the exact same as standard GCD, but with
  # the polynomials monic representation
def compositeModulusGCD(a, b):
    if(b == _sage_const_0 ):
        return a.monic()
    else:
        return compositeModulusGCD(b, a % b)

def CoppersmithShortPadAttack(e,n,C1,C2,eps=_sage_const_1 /_sage_const_30 ):
    """
    Coppersmith's Shortpad attack!
    Figured out from: https://en.wikipedia.org/wiki/Coppersmith's_attack#Coppersmith.E2.80.99s_short-pad_attack
    """
    import binascii
    P = PolynomialRing(ZZ, names=('x', 'y',)); (x, y,) = P._first_ngens(2)
    ZmodN = Zmod(n)
    g1 = x**e - C1
    g2 = (x+y)**e - C2
    res = g1.resultant(g2)
    P = PolynomialRing(ZmodN, names=('y',)); (y,) = P._first_ngens(1)
    # Convert Multivariate Polynomial Ring to Univariate Polynomial Ring
    rres = _sage_const_0 
    for i in range(len(res.coefficients())):
        rres += res.coefficients()[i]*(y**(res.exponents()[i][_sage_const_1 ]))

    diff = rres.small_roots(epsilon=eps)
    recoveredM1 = franklinReiter(n,e,diff[_sage_const_0 ],C1,C2)
    print(recoveredM1)
    print("Message is the following hex, but potentially missing some zeroes in the binary from the right end")
    print(hex(recoveredM1))
    print("Message is one of:")
    for i in range(_sage_const_8 ):
        msg = hex(Integer(recoveredM1*pow(_sage_const_2 ,i)))
        if(len(msg)%_sage_const_2  == _sage_const_1 ):
            msg = '0' + msg[_sage_const_2 :-_sage_const_1 ]
        if(msg[:_sage_const_2 ]=='0x'):
            msg = msg[_sage_const_2 :]
        try:
            print(binascii.unhexlify(msg))
        except:
            print(binascii.unhexlify('0'+msg))


def testCoppersmithShortPadAttack(eps=_sage_const_1 /_sage_const_25 ):
    from Crypto.PublicKey import RSA
    import random
    import math
    import binascii
    M = "flag{This_Msg_Is_2_1337}"
    M = int(binascii.hexlify(M),_sage_const_16 )
    e = _sage_const_3 
    nBitSize =  _sage_const_8192 
    key = RSA.generate(nBitSize)
    #Give a bit of room, otherwhise the epsilon has to be tiny, and small roots will take forever
    m = int(math.floor(nBitSize/(e*e))) - _sage_const_400 
    assert (m < nBitSize - len(bin(M)[_sage_const_2 :]))
    r1 = random.randint(_sage_const_1 ,pow(_sage_const_2 ,m))
    r2 = random.randint(r1,pow(_sage_const_2 ,m))
    M1 = pow(_sage_const_2 ,m)*M + r1
    M2 = pow(_sage_const_2 ,m)*M + r2
    C1 = Integer(pow(M1,e,key.n))
    C2 = Integer(pow(M2,e,key.n))
    CoppersmithShortPadAttack(e,key.n,C1,C2,eps)

def testFranklinReiter():
    p = random_prime(_sage_const_2 **_sage_const_512 )
    q = random_prime(_sage_const_2 **_sage_const_512 )
    n = p * q # 1024-bit modulus
    e = _sage_const_11 

    m = randint(_sage_const_0 , n) # some message we want to recover
    r = randint(_sage_const_0 , n) # random padding

    c1 = pow(m + _sage_const_0 , e, n)
    c2 = pow(m + r, e, n)
    print(m)
    recoveredM = franklinReiter(n,e,r,c1,c2)
    print(recoveredM)
    assert recoveredM==m
    print("They are equal!")
    return True

N = _sage_const_17370303838481078396867008243308868112257548548059095304083176419843329544293059453520977785834201881316544058052761790042480195917382530503087478512154073955285051612704957561001426537455932438432825389315081737200485166417839753998573473081451603834791415253334463365998854998601877157916654540843809424104242227923498742916025820673577009094160761889056257135441612310708909004386515228803850326325845220127547339982229710596800585045146371251910429634814493586813571760891089473908424811524178069610620015296633934386201883491772987354038148907269759119662847942525255096401374349773830992807068488771538369615601 

E = _sage_const_11 

C1 = _sage_const_16646831158806362802187786053000847261352801407099627746656981114264123084291482087935961192670001789636361880742010535618183534314220263031070941144065110371402447505746517004758102622790324243066396378400917586946919353139062614850945782319128404685532864981377048244949294554932057980152355001919018067262729763614490719982533034554246049279851204024827156143138168212490307695216862836737368783077055248476317242183876942418147147304741277868711942793107820496026090839674446132795424932123971125810013756582530141492598683805356372579158966224469542526376498536480134410937637687299998645887813353420966692508791 

C2 =_sage_const_16642663284727388869359397895910335272404595771284103150936358833231470509861640332583361340545124075244886609346899258782739975148997172295074570753127729508759434428381195625867385590828103084995319972798272253634439508974882475880556987849817425770370990761372886789636999323951617453484184957925135433933493595337090091421803222839756611595987594830775847945534456242467806653835522509335138058889714784179670869987360131362472966955922431532692142416069620336546710451989259697070802523963315535188681552814176454454076107504282177864254923316731884568894436596459435508067440009534686683478813445176905136545485 

CoppersmithShortPadAttack(E,N,C1,C2)

