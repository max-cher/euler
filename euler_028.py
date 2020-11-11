import datetime
from time import time
from math import sqrt; from itertools import count, islice

print("started at:", datetime.datetime.now())
print("\n")
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





sum = 1

side = 1

num = 1

while side < (1001):
	for i in range(4):
		for p in range(side+1):
			num += 1
		sum += num
		#print(num)
	side += 2
	

print(sum)


#print(sum)


stopTime = time()
totalTime = timeBetween(startTime, stopTime)

print('\ntotal time:', totalTime)




#
#print("\nstoped at:")
#print(datetime.datetime.now())
