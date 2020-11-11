import datetime
from math import sqrt; from itertools import count, islice
from time import gmtime, strftime, time


print("started at: ",datetime.datetime.now(), '\n', sep='')
startTime = time()

def timeBetween(timeStart, timeStop):
	sec = abs(timeStop - timeStart)
	min = sec//60
	sec -= min*60
	h = min//60
	min -= h*60
	days = h//24
	h -= days*24
	return '{0} days, {1} hours, {2}mins, {3} sec'.format(int(days), int(h), int(min), sec)


def collatz(n):
	i = 0
	while n != 1:
		if n%2 == 0:
			n = n/2
		else:
			n = n*3 + 1
		i += 1
	return i+1


max = 1
max_l = collatz(max)
tmp_l = 0

i_max = 1000000 - 1


for i in range(i_max, 1, -1):
	tmp_l = collatz(i)
	if max_l < tmp_l:
		max = i
		max_l = tmp_l
		
		#print(max, '	', collatz(max))
	



print('\nmax. starting item: {0}\nmax. line: {1}'.format(max, collatz(max)))





stopTime = time()
totalTime = timeBetween(startTime, stopTime)

print('\ntotal time:', totalTime)



