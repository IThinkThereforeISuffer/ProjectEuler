def isPrime(nbr):
	if nbr <= 1:
		return False
	if nbr <=3:
		return True
	if nbr % 2 == 0 or nbr % 3 == 0:
		return False
	i = 5
	while i*i <= nbr:
		if nbr % i == 0 or nbr % (i+2) == 0:
			return False
		i += 6
	return True
cpt = 2
i = 6
while cpt < 10005:
	if isPrime(i - 1):
		cpt += 1 
		if cpt == 10001:
			print(i - 1)
	if isPrime(i + 1):
		cpt += 1
		if cpt == 10001:
			print(i + 1)
	i+=6
print(cpt)