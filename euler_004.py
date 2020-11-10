
li = range(317, 1000)
#li = li.reverse0)
lj = range(317, 1000)
#lj = lj.reverse()

#m = 0
#n = 0
mm = 0
mi = 0
mj = 0

for i in li:
	for j in lj:
		m = i*j
		ml = [int(n) for n in str(i*j)]
		if(ml[0] == ml[5] and ml[1] == ml[4] and ml[2] == ml[3]):
			if(mm < m):
				mm = m
				mi = i
				mj = j
			#print(m)
			#break
			#break
print(mm)
print(mi)
print(mj)


#[int(x) for x in str(num)] 
