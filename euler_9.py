import datetime

print("started at:")
print(datetime.datetime.now())
print("\n")

end = False

for a in range(1, 1000):
	for b in range(1, 1000):
		for c in range(1, 1000):
			if((a<b) and (b<c) and (a*a+b*b == c*c) and (a+b+c == 1000)):
				print(a)
				print(b)
				print(c)
				print(a*b*c)
				end = True
				break
		if(end):
			break
	if(end):
		break



	
print("\nstoped at:")
print(datetime.datetime.now())
