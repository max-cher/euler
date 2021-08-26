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


def fac(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
    return a



def is_fac_num(x):
    nums = []
    num = x
    while num:
        nums.append(num%10)
        num //= 10
    summ = 0
    for i in nums:
        summ += fac(i)
    if summ == x:
        return True
    return False



A = []
stop = 1000000


for i in range(3, stop):
    if is_fac_num(i):
        A.append(i)


summ = 0
for i in A:
    summ += i

print(A)
print(summ)







stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

