def divThree(n):
	if n % 3 == 0:
		return True
	else:
		return False
def divFive(n):
	if n % 5 == 0:
		return True
	else:
		return False
n=1000
set3 = set()
set5 = set()
for i in range(n):
	if divThree(i):
		set3.add(i)
	if divFive(i):
		set5.add(i)
total = set3.union(set5)
sum = 0
for x in total:
	sum += x
print(total)
print(sum)