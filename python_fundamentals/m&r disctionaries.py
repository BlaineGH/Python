aboutme = {}
aboutme["first"] = "blaine"
aboutme["last"] = "rogers"
aboutme["age"] = "26"
aboutme["country"] = "USA"
aboutme["language"] = "python"

print 'my name is', aboutme["first"]
print 'my age is', aboutme["age"]
print 'my country of birth is', aboutme["country"]
print 'my favorite language is', aboutme["language"]

for key,data in aboutme.iteritems():
	print key, '=', data