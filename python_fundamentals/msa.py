x = []
for i in range(1,1000):
	if (i % 2 != 0):
		x.append(i)
print(x)		
	
y = []
for i in range(5,100000):
	if(i % 5 == 0):
		y.append(i)
print(y)

a = [1, 2, 5, 10, 255, 3]
print sum(a)

sum = 0
for i in a:
	sum+= i
print sum

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
	sum+=i
	avg = sum/len(a)
print avg