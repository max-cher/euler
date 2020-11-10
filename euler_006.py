import datetime

print("started at:")
print(datetime.datetime.now())
print("\n")


a = 0
b = 0

for i in range(1, 101):
	a = a + i*i

for i in range(1, 101):
	b = b + i

b = b*b

print(a)
print(b)

c = b - a

print(c)
	
print("\nstoped at:")
print(datetime.datetime.now())
