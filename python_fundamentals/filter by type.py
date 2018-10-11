def function(x):
	if isinstance(x, str) == True:
		if len(x) >= 50:
			print "Thats a big sentence!"
		else:
			print "Thats a small sentence"
	elif isinstance(x, int) == True:
		if x >= 100:
			print "Thats a big number!"
		else:
			print "Thats a small number"
	elif isinstance(x, list) == True:
		if len(x) >= 10:
			print "That's a big list!"
		else:
			print "Thats a short list"

function()