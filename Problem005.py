def pgcd(a,b):
	if b == 0:
		return a
	else:
		r = a % b
		return pgcd(b,r)
def ppcm(a,b):
	d = pgcd(a,b)
	return int(a*b / d)
p = 1
for i in range(20):
	p = ppcm(p,i+1)

print(p)
