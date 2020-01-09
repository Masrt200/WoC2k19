import operator

alphabet='abcdefghijklmnopqrstuvwxyz'
digraphs={}
pos={}
diff=[]
ciphertext='Moho wb 1997, tsma zscredsf Eojse Vozaox\'g Mcbnpb ygtwmfg bfqsswsr b qyqm yg hrf tssgh cccu wb xvod kcemr lfqcwf Fyxzwxh\'c gsbjsg pt cfjsx Vobsm Zphhos bywszc. Hrf pypy, Iofbz Dyuhsb obn hvo Dvsmcgyqvsb\'g Thcxf, gbg bfzsqbhsn hc b zyx-dbjcfsum lpcyciszp, krffs jh gbg njgqywsfoe pi o cfqfouofi kvy fske wd obn uoff wd hc Ismwbb gjhv b dytwhsws bfjwox. Mpbgorisxuzm, Vsinob, kvy von cfshwbkmzm ewgvjysn \"dis bvppstv djhzo\", sson hvo pcyl vsngsvg. Rjuvvz wwqfsctsr cm Bpkzsou\'t kysy, is lfuox hvo dfydsgc hvku zoe hy cbo ct uvs ncgd gimdsgcgiz dwbonohsd tbbbqrjgsc ct bzz uwao.[10] Vozaox\'g fbhrvgwkta vfr dp Fyxzwxh\'c 1999 gkms yg hrf tsma bjuvdt tys hrf tssgh gcib Vobsm Zphhos pypyg uc Gbfbos Pbpg. gcf b foqcfdfr £1 asmzwyo (ET$2,000,000).[11] O esakor Bpkzsou wbrs xog uvod hvo dfsoqwzbz mbgh cs ufdh thfsdhzi Pfsuwgr, ovmcksou xfjsbuvsvfgg gcf uvs jbqvvgwyo cp aoxz Wbjgv bqhysg, tiqr og Swqrbfr Iofbjg kt Renpzoecfo, oxe tys qkthwxh cp Tfooqv bbr Fogdffb Fifyqsox oqdpfg jb Rbffi Dcdusf bbr uvs Hcpvfh yg Tsss gisfo qvksoqdffg gfcw hvo pcyl obf gzfqwpjsr bg cvqv.[12] Fcgmwbq koc vscjhoxu hy gsvm hrf fshvhc psmbigo gvo "rseb\'u kkoh dp usws disa dcbdscz pjsb hvo fscu cp hvo ghysm\" pm tszvjbu uvs swurug dp hrf qrbfomusfc, krjqv xcive vkws ooopvfr Gbfbos Pbpg. uc wbys ocb-bihrpf-gswhdfb cfeiomg.'.lower()
maxx=[]

for x in alphabet:
	for y in alphabet:
		digraphs[x+y]=0
		pos[x+y]=[]


x=0
while x<len(ciphertext)-1:
	y=x+1
	X=ciphertext[x]
	Y=ciphertext[y]
	if X in alphabet and Y in alphabet:
		di=X+Y
		digraphs[di]+=1
		pos[di].append(x)
		x+=2
	else:
		x+=1

for x,y in pos.items():
	if len(y)>=2:
		i=0
		while i<len(y)-1:
			gap=y[i+1]-y[i]
			diff.append(gap)
			i+=1
			#print(gap,end=' ')
		#print()

digraphs = sorted(digraphs.items(), key=operator.itemgetter(1),reverse=True)

x=0
while x<5:
	maxx.append(digraphs[x][0])
	x+=1

common=['th','er','on','an','ss']

#print(maxx)

guess=[]
for x in  common:
	for y in maxx:
		possible=''
		possible+=chr((ord(y[0])-ord(x[0]))%26+97)+chr((ord(y[1])-ord(x[1]))%26+97)
		guess.append(possible)
	print(guess)
	guess=[]