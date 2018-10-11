
def function(list1, list2):
	if len(list1) != len(list2):
		i= "not the same length"
		return i
	for x in range(0,len(list1)):
		if list1[x] != list2[x]:
			 i="wrong"
			 return i 
	i= "they are the same"
	return i

		
i=function([1,2,5,6,2], [1,2,5,6,2])
print i