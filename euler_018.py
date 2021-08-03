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

#pathname = 'p018_triangle_example.txt'
#pathname = 'p018_triangle.txt'
pathname = 'p067_triangle.txt'

T = []
with open(pathname, 'r') as file:
    L = file.readlines()
    for line in L:
        T.append(line.split())

T = [[int(num) for num in lstt[:]] for lstt in T]



def calc_paths(x, y):
    local_paths = []
    local_paths.append(T[y][x] + T[y+1][x])
    local_paths.append(T[y][x] + T[y+1][x+1])
    return max(local_paths)



def calc_lines(y):
    line = []
    for i in range(len(T[y])):
        line.append(calc_paths(i, y))
    T.pop()
    T[y] = line



while(len(T) > 1):
    calc_lines(len(T)-2)
print('T:', T)




stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

