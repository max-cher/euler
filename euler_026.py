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



def len_of_seq(A):
    result = 0
    L = 0
    for i in range(1, len(A)-1, 1):
        l_tmp = 0
    
    
    return result

def foo(x):
    max_len = 0
    d = 0
    for i in range(1, x, 1):
        line = str(1*10**1000//i)
        line_len = len_of_seq(line)
        if line_len > max_len:
            max_len = line_len
            d = i
        print(line)
        #A.append(line)
    return d, max_len

print(foo(10))

#print(A)


stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

