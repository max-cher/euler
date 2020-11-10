import datetime

print("started at:")
print(datetime.datetime.now())
print("\n")

end = False

def is_prime(x):
	if(x == 1):
		return(0)
	j = 1
	while(j < x-1):
		j+=1
		if(x%j == 0):
			return(0)
	return(1)

s = 2

a = 3

#for a in range(1, 100000):
while(a < 50000):
	if(is_prime(a)):
		s += a
		
	a += 2

print(s)
	
print("\nstoped at:")
print(datetime.datetime.now())
