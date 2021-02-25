from pwn import *
from Crypto.Util.number import inverse,long_to_bytes

def root(n, k):
      low = 0
      high = n + 1
      while high > low + 1:
         mid = (low + high) >> 1
         mr = mid**k
         if mr == n:
            return (mid, 1)
         if mr < n:
            low = mid
         if mr > n:
            high = mid
      return (low, 0)


def HASTAD(N,C,lim):
	EN=1
	for i in N:
		EN*=i

	NN=[]
	for i in range(lim):
		a=1
		for j in range(lim):
			if j!=i:
				a*=N[j]
		NN.append(a)

	B=[]
	for i in range(lim):
		inv=inverse(NN[i],N[i])
		B.append(inv)

	T=[]
	for i in range(lim):
		ttt=C[i]*NN[i]*B[i]
		T.append(ttt)

	CC=sum(T)%EN

	return CC

lim=17

N=[]
C=[]

r=remote('shell.ctf.gunnhacks.com', 42843)

for i in range(lim):
	r.recv(2048)
	r.sendline('1')
	print(i)
	#print(r.recv(8192))
	n=int(r.recvline()[4:-1].decode())
	e=int(r.recvline()[4:-1].decode())
	c=int(r.recvline()[4:-1].decode())
	N.append(n)
	C.append(c)

M=root(HASTAD(N,C,lim),lim)[0]

print(long_to_bytes(M))

#gunnHacks{sm0l_e_strikes_again_18c5ff37}