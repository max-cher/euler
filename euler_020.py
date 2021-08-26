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



tgt = 100

def fac(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res

summ = 0
for i in str(fac(tgt)):
    summ += int(i)

print(summ)

stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

