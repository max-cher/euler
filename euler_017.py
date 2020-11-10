from math import sqrt; from itertools import count, islice
import datetime

print("started at:")
print(datetime.datetime.now())
print('\n')



def isPrime(n):
	if n < 2: return False
	for number in islice(count(2), int(sqrt(n)-1)):
		if not n%number:
			return False
	return True



def letInNum(x):
	s = 0
	l = ''

	if(x > 999):
		if((x//1000) == 1):
			s += 1
			x -= 1000
			l += 'one thousand '
			
		elif((x//2000) == 1):
			s += 1
			x -= 2000
			l += 'two thousand '
			
		elif((x//3000) == 1):
			s += 1
			x -= 3000
			l += 'three thousand '
			
		elif((x//4000) == 1):
			s += 1
			x -= 4000
			l += 'four thousand '
			
		elif((x//5000) == 1):
			s += 1
			x -= 5000
			l += 'five thousand '
			
		elif((x//6000) == 1):
			s += 1
			x -= 6000
			l += 'six thousand '
			
		elif((x//7000) == 1):
			s += 1
			x -= 7000
			l += 'seven thousand '
			
		elif((x//8000) == 1):
			s += 1
			x -= 8000
			l += 'eight thousand '
			
		elif((x//9000) == 1):
			s += 1
			x -= 9000
			l += 'nine thousand '
			
	if(x > 99):
		if((x//100) == 1):
			s += 1
			x -= 100
			l += 'one hundred and '
			
		elif((x//200) == 1):
			s += 1
			x -= 200
			l += 'two hundred and '
			
		elif((x//300) == 1):
			s += 1
			x -= 300
			l += 'three hundred and '
			
		elif((x//400) == 1):
			s += 1
			x -= 400
			l += 'four hundred and '
			
		elif((x//500) == 1):
			s += 1
			x -= 500
			l += 'five hundred and '
			
		elif((x//600) == 1):
			s += 1
			x -= 600
			l += 'six hundred and '
			
		elif((x//700) == 1):
			s += 1
			x -= 700
			l += 'seven hundred and '
			
		elif((x//800) == 1):
			s += 1
			x -= 800
			l += 'eight hundred and '
			
		elif((x//900) == 1):
			s += 1
			x -= 900
			l += 'nine hundred and '


	if(x > 19):
		if((x//20) == 1):
			s += 4
			x -= 20
			l += 'twenty-'
			
		elif((x//30) == 1):
			s += 4
			x -= 30
			l += 'thirty-'
			
		elif((x//40) == 1):
			s += 4
			x -= 40
			l += 'forty-'
			
		elif((x//50) == 1):
			s += 4
			x -= 50
			l += 'fifty-'
			
		elif((x//60) == 1):
			s += 4
			x -= 60
			l += 'sixty-'
			
		elif((x//70) == 1):
			s += 4
			x -= 70
			l += 'seventy-'
			
		elif((x//80) == 1):
			s += 4
			x -= 80
			l += 'eighty-'
			
		elif((x//90) == 1):
			s += 4
			x -= 90
			l += 'ninety-'
			

	if(x > 9):
		if(x == 11):
			s += 3
			x -= 11
			l += 'eleven'
			
		elif(x == 12):
			s += 3
			x -= 12
			l += 'twelve'
			
		elif(x == 13):
			s += 5
			x -= 13
			l += 'thirteen'
			
		elif(x == 14):
			s += 4
			x -= 14
			l += 'fourteen'
			
		elif(x == 15):
			s += 4
			x -= 15
			l += 'fifteen'
			
		elif(x == 16):
			s += 3
			x -= 16
			l += 'sixteen'
			
		elif(x == 17):
			s += 5
			x -= 17
			l += 'seventeen'
			
		elif(x == 18):
			s += 5
			x -= 18
			l += 'eighteen'
			
		elif(x == 19):
			s += 4
			x -= 19
			l += 'nineteen'
	else:
		if(x == 0):
			s += 4
			x -= 0
			l += 'zero'
			
		elif(x == 1):
			s += 3
			x -= 1
			l += 'one'
			
		elif(x == 2):
			s += 3
			x -= 2
			l += 'two'
			
		elif(x == 3):
			s += 5
			x -= 3
			l += 'three'
			
		elif(x == 4):
			s += 4
			x -= 4
			l += 'four'
			
		elif(x == 5):
			s += 4
			x -= 5
			l += 'five'
			
		elif(x == 6):
			s += 3
			x -= 6
			l += 'six'
			
		elif(x == 7):
			s += 5
			x -= 7
			l += 'seven'
			
		elif(x == 8):
			s += 5
			x -= 8
			l += 'eight'
			
		elif(x == 9):
			s += 4
			x -= 9
			l += 'nine'
	return(l)
			



while(1):
	a = int(input('Enter some number: '))

	print(letInNum(a))


print("\nstoped at:")
print(datetime.datetime.now())
