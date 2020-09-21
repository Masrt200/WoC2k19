def skip(some_text,E_D):
	j=1
	soln_text=''
	if E_D !=None:
		soln_text=(some_text*E_D)[::E_D]
	else:
		while j<len(some_text):
			try_text=some_text*j
			soln_text+='Jump {}: '.format(j) + try_text[::j] + '\n'  
			j+=1

	return soln_text

