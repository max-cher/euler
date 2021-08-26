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

min = 2
max = 100

for a in range(min, max+1):
    for b in range(min, max+1):
        A.append(a**b)
        #print('{0} ^ {1}'.format(a, b))

A.sort()
B = [A[0]]
for i in range(len(A)-1):
    if A[i] != A[i+1]:
        B.append(A[i+1])
        #A.pop(i + 1)

#print(B)
print(len(B))


stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

