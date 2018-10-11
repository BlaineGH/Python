import random
print 'Score and Grades'
def function(x):
	for i in range(x):
		x = random.randint(60,100)
		if (x>=90):
			print ('Score:',x,'Your grade is a A')
		elif (x>=80):
			print ('Score:',x,'Your grade is a B')
		elif (x>=70):
			print ('Score:',x,'Your grade is a C')
		elif (x>=60):
			print ('Score:',x,'Your grade is a D')
function(10)
print 'End of program. Bye!'