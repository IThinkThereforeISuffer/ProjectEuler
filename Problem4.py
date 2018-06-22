def isPalindrom(n):
	pal = str(n)
	i = 0
	while i <= len(pal)/2:
		if pal[i] != pal[len(pal) - i - 1]:
			return False
		i+=1
	return True
pal = set()
stop = False
i = 999
while i > 99:
	j = 999
	while j > 99:
		if isPalindrom(i*j):
			pal.add(i*j)
		j -= 1
	i -= 1	
print (i)
print(j)
print(pal)
print(max(pal))