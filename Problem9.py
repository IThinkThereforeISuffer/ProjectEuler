def pythagore(a,b,c):
	if a*a + b*b == c*c:
		return True
	else: 
		return False
b = 1
bees = set()
while b < 500:
	b +=1
	if (1000*(500-b) % (1000-b)) == 0:
		bees.add(b)
a = int(1000*(500-b) % (1000-b))
for x in bees:
	a = int(1000*(500-x) / (1000-x))
	c = 1000 - a - x 
	if pythagore(a,x,c):
		print(a*x*c)