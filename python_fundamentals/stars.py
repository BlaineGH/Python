def draw_stars(a):
	pass
	for i in range(len(a)):
		if (type(a[i]) == str):
			print (a[i][0])*len(a[i])
		else:
			print ('*')*a[i]
draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

