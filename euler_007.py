import datetime
import time

print("started at:")
print(datetime.datetime.now())
print("\n")

start = time.time()

def is_prime(x):
	j = 1
	while(j < x-1):
		j+=1
		if(x%j == 0):
			return(0)
	return(1)

i = 2
c = 0

while(1):
	if(is_prime(i)):
		c +=1
	if(c == 10001):
		print(i)
		break
	i+=1
	


	
print("\nstoped at:")
print(datetime.datetime.now())

stop = time.time() - start

print('затрачено {0} секунд'.format(stop))


