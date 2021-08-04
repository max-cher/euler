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


tgt = 1000000
counter = 1
max_num = 9

A = []
for i in range(max_num+1):
    A.append(i)
print(A)


def find_index(A, x):
    for i in range(len(A)-1, -1, -1):
        if A[i] < x:
            return i
    print('###########')
    return(-1)


def to_min(A):
    A.sort()
    return A


def swap(A):
    for i in range(1, max(A)):
        tmp = A[0] + i
        if tmp in A:
            index = A.index(A[0] + i)
            break
    
    A[0], A[index] = A[index], A[0]
    return A


def next(a):
    #max_num = len(a) - 1
    left = len(a) - 2
    
    if a[left+1] > a[left]:
        a[left+1], a[left] = a[left], a[left+1]
        return a
    
    
    left = len(a) - 3
    #print(left)
    while max(a[left+1:]) < a[left]:
        left -= 1
    if max(a[left+1:]) > a[left]:
        a[left:] = swap(a[left:])
        a[left+1:] = to_min(a[left+1:])
        return a
    
    print('ERR: ', end='')
    
    #a[0] += a[1]
    #tmp = a.pop()
    #print('tmp:', a, '+', tmp)
    #index = find_index(a, tmp)
    #while index == -1:
    #    tmp_0 = a.pop()
    #    a.insert(tmp)
    #    tmp = tmp_0
    #    index = find_index(a, tmp)
    #print('index:', index)
    #if index < 0:
    #    a.append(a.pop(0))
    
    #a.insert(index, tmp)
    
    return a


while counter < tgt:
    A = next(A)
    
    #tmp = A.pop()
    #A.insert(-counter, tmp)
    #A[2] += 1
    
    #print(A)
    counter += 1
    
print(counter)
print(A)

#counter = 0

#for i in range(211):
#    a = str(i)
#    if a.count('0') == 1 and a.count('1') == 1 and a.count('2') == 1:
#        print(i)

from math import factorial as fuck

def calc(tgt, max):
    tgt -= 1
    result = []
    for i in range(max, 0, -1):
        #print(i, tgt)
        result.append(str(int(tgt//fuck(i))))
        tgt %= fuck(i)
    
    #result.append(str(int(tgt)))
    #print(result)
    for i in range(max+1):
        if str(i) not in result:
            #print('Add:', i)
            result.append(str(i))
    return(''.join(result))
    
#for i in range(2, 25, 1):
#    print(calc(i, 3))


def is_unical(num:str):
    example = ''
    for i in range(len(num)):
        example += str(i)
    #print(example)
    for i in num:
        if i not in example:
            return False
        if num.count(i) > 1:
            return False
    #return False
    return True


def gen_list(max_digit, tgt):
    #result = []
    counter = 1
    for i in range(10**(max_digit+1)):
        tmp = '{0:0{1}}'.format(i, max_digit+1)
        if is_unical(tmp):
            if counter == tgt:
                return(tmp)
            counter += 1

#for i in gen_list(3):
#    print(i)

#print(gen_list(8, 2))








stopTime = time()
totalTime = timeBetween(startTime, stopTime)
print('\ntotal time:', totalTime)

