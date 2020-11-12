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

pathname = 'p018_triangle_example.txt'

T = []
L = []
#line = ''

with open(pathname, 'r') as file:
    #while(True):
    #    line = file.readline()
    #    if not line:
    #        break
    #    T.append(line.split())
        
    L = file.readlines()
    for line in L:
        T.append(line.split())

last_line = len(T) - 1
print('triangle has {0} lines'.format(len(T)))
print('last line is {0}'.format(last_line))

#print(T)
#print(len(T))

def max_path(P):
    
    return len(P[0])
    #pass

def calc_paths(x, y):
    #print(T[y][x])
    paths = []
    paths.append(1)
    paths.append(1)
    return paths

#for element in T[len(T) - 1]:
#    print(element)



for i in range(len(T[last_line])):
    #print(T[last_line][i])
    paths = []
    paths.append(calc_paths(i, last_line))
    
print('Answer: {0}'.format(max_path(paths)))
#print(len(T[len(T) - 1]))






stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

