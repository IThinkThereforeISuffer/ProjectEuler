def summ(n):
	return int(n*(n+1) / 2)
def sumSquare(n):
	return summ(n)*summ(n)
def squaresSum(n):
	square = 0
	for i in range(n+1):
		square += i*i
	return square

n = 100
squS = squaresSum(n)
sSqu = sumSquare(n)
print(sSqu - squS)