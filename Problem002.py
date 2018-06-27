def fibo(n):
	if n == 0:
		return 1
	else:
		if n == 1:
			return 2
		else:
			return fibo(n-1) + fibo(n-2)
n = 10
setfib = set()
num = 0
i = 0
while (num < 4000000):
	num = fibo(i)
	if num % 2 == 0:
		setfib.add(num)
	i += 1

sum = 0
for x in setfib:
	sum += x

print(setfib)
print(sum)
