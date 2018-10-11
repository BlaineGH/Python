import random
print 'Starting Program...'
def function(x):
	pass
	heads = 0 
	tails = 0
	for i in range(1,x+1):
		x = random.random()
		if ( x > .5):
			heads = heads + 1
		elif (x < .5):
			tails = tails + 1
		print ('Attempt #',i,': Throwing a coin... Heads!... Got ',heads,' heads and ', tails,' tails so far!')
function(5000)
print 'Ending program, Thank you!'