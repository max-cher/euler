


f0 = 1
f1 = 2

n = 1000

i = 2

while(1):
	f0, f1 = f1, f0
	f1 += f0
	
	i += 1

	
	if(len(str(f0)) > (n-1)):
		print(f0)
		print('\n')
		print(i)
		break
