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



def tr(a):
	s = 0
	for i in islice(count(1), a):
		s += i
	return(s)


def divs_old(a):
	d = 0
	for i in islice(count(1), a+1):
		if a%i == 0:
			d += 1
	return d



def divs(a):
	d = 1
	for i in range(2, int(sqrt(a))):
		if(a%i == 0):
			d += 1
	d *= 2
	if sqrt(a)%1 == 0:
		d += 1
	return(d)

def divsSum(x):
	sum = 0
	d = 0
	for i in range(1, x):
		if x%i == 0:
			sum += i
	return sum

def isBig(x):
	return x < divsSum(x)




border = 28123

num1 = []
num2 = []

for i in range(border):
	if isBig(i):
		pass
		#num1.append(i)
		#num2.append(i)





n = 12

print(n, divsSum(n))

print(isBig(13))

print(len(num1))





stopTime = time()
totalTime = timeBetween(startTime, stopTime)

print('\ntotal time:', totalTime)




#
#print("\nstoped at:")
#print(datetime.datetime.now())
