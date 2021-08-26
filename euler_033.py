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


def check(a, b):
    
    #a1 = str(a)
    #b1 = str(b)
    if a[0] == b[0]:
        a = a[1:]
        b = b[1:]
    if a[0] = b[1]:
        a = a[1:]
        b = b[:1]
    
    if a[1] == b[0]:
        a = a[:1]
        b = b[1:]
    if a[1] = b[1]:
        a = a[:1]
        b = b[:1]
    
    #if b 
    
    return False


for a in range(10, 100):
    for b in range(10, 100):
        if check(a, b):
            A.append([a, b])


stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

