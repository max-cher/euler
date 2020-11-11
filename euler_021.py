import datetime
from math import sqrt; from itertools import count, islice
from time import gmtime, strftime


print("started at:\n",datetime.datetime.now(), '\n############################################\n')
t0 = strftime("%H%M%S")




def d(n):
	
	sum = 0
	
	for i in range(1, n):
		if n%i == 0:
			sum += i
	
	
	
	return sum


summ = 0

for i in range(1, 10000):
	if i != d(i) and i == d(d(i)):
		summ += i
		print(i)

print(summ)


print("\n############################################\nstoped at:\n",datetime.datetime.now())
t1 = strftime("%H%M%S")
h = int(t1[0:2]) - int(t0[0:2])
m = int(t1[2:4]) - int(t0[2:4])
s = int(t1[4:6]) - int(t0[4:6])

if(s < 0):
	s += 60
	m -= 1
if(m < 0):
	m += 60
	h -= 1
if(h < 0):
	h += 24



print('\ntotal time is: ', str(h),'h',str(m),'m',str(s),'s')





