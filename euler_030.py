import datetime
from time import time

#import itertools

print('started at:', datetime.datetime.now(), '\n')
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



A = []

power = 5

for i in range(2, 1000000):
    line = '{0:04}'.format(i)
    summ = 0
    for x in line:
        summ += int(x)**power
    if i == summ:
        A.append(i)

print(A)

summ = 0
for i in A:
    summ += i

print(summ)




stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

