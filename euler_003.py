import datetime
from time import time
from math import sqrt; from itertools import count, islice
#total time is: 6.934788227081299 sec.


i = 2
m = 0
d = 600851475143
d = 190056425687

startTime = time()

def is_simple(x):
	j = 1
	while(j < x-1):
		j+=1
		if(x%j == 0):
			return(0)
	return(1)

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

#print(is_simple(4))

print("started at:")
print(datetime.datetime.now())

#for i in range(1, d):

while i < int(d/2):
	i = i+1
	if((d%i == 0) and is_simple(d/i)):
		#if(is_simple(d/i)):
		m = d/i
		print("\nresult is:")
		print(m)
		break
#print("\nresult is:")
#print(m)
#print(i)


print("\nstoped at:")
print(datetime.datetime.now())

stopTime = time()

totalTime = stopTime - startTime

print('total time is: {0} sec.'.format(totalTime))
