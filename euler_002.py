s = 0
f0 = 1
f1 = 2

while f0 < 4000000:
	if f0%2 ==0:
		s += f0
	f0, f1 = f1, f0
	f1 += f0

print(s)

