def odd_even(x):
	pass
for x in range(1,2001):
	if (x % 2 == 0):
		print ('Number is ',x,' This is a even number')
	elif (x % 2 != 0):
		print ('Number is',x,' This number is odd')
odd_even(2000)

def multiply(a,b):
	for i in range(len(a)):
		a[i] *= b
	return a
a = [2,4,10,16]
b = multiply(a, 5)	
print b

def layered_multiples(a):
	newarr = []
	for elm in a:
		newlist = []
		temp = elm
		while temp > 0:
			newlist.append(1)
			temp = temp - 1
			if temp == 0:
				newarr.append(newlist)
	return newarr
x = layered_multiples(multiply([2,4,5],3))
print x

