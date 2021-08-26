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


def is_pan(num:str):
    if len(num) > 9 or '0' in num:
        return False
    example = ''
    for i in range(1, len(num)+1):
        example += str(i)
    #print(example)
    for i in num:
        #if i not in example:
        #    return False
        if num.count(i) > 1:
            return False
    #return False
    return True


def clear_duplicats(M):
    R = []
    for i in M:
        if R.count(i) == 0:
            R.append(i)
    return R


for a in range(1, 5000):
    for b in range(1, 5000):
        line = str(a) + str(b) + str(a*b)
        if is_pan(line):
            A.append(a*b)
            #print(line)
            #summ += a*b

#print(summ)

#for i in A:
#    print(i)

#print('###############')
#print(len(A))
A = clear_duplicats(A)
print(len(A))
print('###############')

summ = 0

for i in A:
    summ += i

print(summ)



stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

