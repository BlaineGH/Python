char = 'o'
def findchar(var):
	newstr=[]
	for element in var:
		if char in element:
			newstr.append(element)
	print newstr
findchar(['hello','world','my','name','is','Anna'])

