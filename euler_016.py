import datetime
from math import sqrt; from itertools import count, islice
from time import gmtime, strftime


print("started at:\n",datetime.datetime.now(), '\n############################################\n')
t0 = strftime("%H%M%S")






a = 2**1000

l = str(a)

s = 0

for i in range(0, len(l)):
	s += int(l[i])

print(s)









print("\n############################################\nstoped at:\n",datetime.datetime.now())
t1 = strftime("%H%M%S")
#t0 = '235030'
#t1 = '000230'
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





