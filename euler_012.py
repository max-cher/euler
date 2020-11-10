from math import sqrt; from itertools import count, islice
import datetime



print("started at:")
print(datetime.datetime.now())
print('\n')


def tr(a):
	s = 0
	for i in range(1, a+1):
		s += i
	return(s)

def divs(a):
	d = 0
	for i in range(1, a+1):
		if(a%i == 0):
			d += 1
	return(d)
	


i = 1
lo = 0
hi = 1

n = 7
			#divs


while(divs(tr(i)) < n):
	i *= 2
	print(i)
hi = i
lo = i/2
i = int(lo + (hi - lo)/2)

print('##########')

while((hi - lo) > 2):
	
	if(divs(tr(i)) > n):
		hi = i

	elif(divs(tr(i)) < n):
		lo = i
	
	i = int(lo + (hi - lo)/2)
	print(i)

print(i)

if(divs(tr(i)) > n):
	#print(i)
	i *= 2
else:
	i *= 2
	#print(i*2)

print(i)
print(tr(i))
print(divs(tr(i)))

print('\n')
print(i-1)
print(tr(i-1))
print(divs(tr(i-1)))



print(divs(28))


print("\nstoped at:")
print(datetime.datetime.now())



#divs - возвращает число делителей
#i - пробное число, для которого пробуем угадать число делителей более 500
#если divs(i) < 500: умножаем i на 2 - прыгаем в два раза
#как только перепрыгнем - начнется магия
#если divs(i) > 500: либо угадали, либо перепрыгнули
#lo = i предыдущее; hi = i; i = lo + (hi - lo)/2
#цикл пока hi - lo > 1
#если divs(i) > 500: значит, все еще перелет - ответ левее. значит, hi = i, i = lo + (hi - lo)/2
#если divs(i) < 500: значит, мало - ответ правее. значит, lo = i; i = lo + (hi - lo)/2
#
#
#
#
#
#
#






