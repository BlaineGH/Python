def function(i):
	sum=0
	newstr=''
	temp = []
	temp2 = ""
	for x in range(0,len(i)):
		if  isinstance(i[x], int):
			sum+=i[x]
		elif isinstance(i[x], float):
			sum+=i[x]
		elif isinstance(i[x], str):
			newstr+=i[x] + ' '
	if sum == 0:
		print "just a string"
	elif newstr == '':
		print "just numbers"
	else:
		print "mixed list"
	
	print sum
	print newstr


function()
