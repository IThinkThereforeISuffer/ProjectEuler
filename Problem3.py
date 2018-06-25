def isPrime(n):
	if n <= 1:
		return False
	else: 
		if n <= 3:
			return True
		else:
			if n % 2 == 0 or n % 3 == 0:
				return False
	i = 5
	while i*i <= n:
		if n % i == 0 or n % i+2 == 0:
			return False
		i += 6
	return True

def maxPrimeFactor(n):
	i = 2
	maxi = 0
	while i*i <= n:
		if n % i == 0 and isPrime(i):
			maxi = i
		i += 1
	return maxi

print(maxPrimeFactor(600851475143))