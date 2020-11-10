import datetime

print("started at:")
print(datetime.datetime.now())
print("\n")


n = 1



while(1):
	
	r = True
	for i in range(2, 22):
		
		if(n%i != 0):
			r = False
			break
	if(r):
		print(n)
		break
	n +=1
			 
	
print("\nstoped at:")
print(datetime.datetime.now())
