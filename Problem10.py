import math 
def eratosthenes(n): 
# the Sieve of Eratosthenes algorithm. 
	plist = [True] * n 
	plist[0] = False 
	plist[1] = False 
	for i in range(2, int(math.sqrt(n)) + 1): 
		toRemove = i * 2 
		while toRemove < n: 
			plist[toRemove] = False 
			toRemove += i 
	prime = [] 
	for i in range(n): 
		if plist[i] == True: 
			prime.append(i) 
	return prime 

primeNum = eratosthenes(2000000) 
print(sum(primeNum))