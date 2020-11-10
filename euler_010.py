from math import sqrt; from itertools import count, islice
import datetime



print("started at:")
print(datetime.datetime.now())
print('\n')

def isPrime(n):
	if n < 2: return False
	for number in islice(count(2), int(sqrt(n)-1)):
		if not n%number:
			return False
	return True

i = 3
s = 2

#for i in range(2, 2000000):
while(i < 2000000):
	if(isPrime(i)):
		s += i
	i += 2

print(s)


print("\nstoped at:")
print(datetime.datetime.now())
