import datetime
from time import time
from math import sqrt; from itertools import count, islice


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


def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


def is_cuteble_prime(x):
    
    # right cut
    tmp_num = x
    while tmp_num:
        #print(tmp_num)
        if not isPrime(tmp_num):
            return False
        tmp_num //= 10
    #print('right passed')
    # left cut
    len_num = len(str(x)) - 1
    
    tmp_num = x
    while tmp_num:
        #print(tmp_num)
        #tmp_num %= 10**len_num
        if not isPrime(tmp_num):
            #print('{0} not prime!'.format(tmp_num))
            return False
        tmp_num %= 10**len_num
        len_num -= 1
    #print('left passed')
    
    return True



A = []

tmp_num = 10

while len(A) < 11:
    #print(tmp_num)
    if is_cuteble_prime(tmp_num):
        A.append(tmp_num)
        print(tmp_num)
    tmp_num += 1




summ = 0
for i in A:
    summ += i

print(A)
print(summ)






stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

