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


SIZE_X = 20
SIZE_Y = 20



A = [0]*(SIZE_X + 1)
for i in range(SIZE_X + 1):
    A[i] = [0]*(SIZE_Y + 1)


summ = 0

def ways(x, y):
    if x == 0 and y == 0:
        return 1
    elif x == 0:
        if 0 == A[x][y]:
            A[x][y] = ways(x, y - 1)
        return A[x][y]#ways(x, y - 1)
    elif y == 0:
        if 0 == A[x][y]:
            A[x][y] = ways(x - 1, y)
        return A[x][y]#ways(x - 1, y)
    else:
        if 0 == A[x][y]:
            A[x][y] = ways(x, y - 1) + ways(x - 1, y)
        return A[x][y]#ways(x, y - 1) + ways(x - 1, y)



print(ways(SIZE_X, SIZE_Y))


i = 0

def fill_arr():
    for Y in range(SIZE_Y + 1):
        for X in range(SIZE_X + 1):
            A[X][Y] = i
            i += 1

def print_arr():
    for Y in range(SIZE_Y + 1):
        print('[', end='')
        for X in range(SIZE_X + 1):
            print(A[X][Y], end='')
        print(']\n', end='')


stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

