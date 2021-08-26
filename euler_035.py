import datetime
from time import time
from math import sqrt; from itertools import count, islice

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



def is_prime(x):
    if x < 2:
        return False
    j = 1
    while(j < x - 1):
        j += 1
        if(x%j == 0):
            return False
    return True

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))




def shift(x):
    if x < 10:
        return x
    tmp = x%10
    x //= 10
    x += tmp*10**(len(str(x)))
    return x
    

def is_circular_prime(x):
    len_num = len(str(x))
    num = x
    
    for i in range(len_num):
        if not isPrime(num):
            return False
        num = shift(num)
    
    return True



A = []
stop = 1000000



for i in range(stop):
    if is_circular_prime(i):
        A.append(i)








#print(A)
print(len(A))




stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

