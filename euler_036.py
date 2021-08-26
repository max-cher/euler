import datetime
from time import time


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




def is_palindrome(line : str):
    for i in range(len(line)//2):
        if line[i] != line[-(i+1)]:
            return False
    return True


stop = 1000000
A = []


for i in range(stop):
    if is_palindrome(str(i)) and is_palindrome(str(bin(i))[2:]):
        A.append(i)


summ = 0
for i in A:
    summ += i

print(A)
print(summ)






stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

