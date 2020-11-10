file = open('p022_names.txt')
line = file.readline()
file.close()


names = []
name = ''

for i in range(0, len(line)):
	if(line[i].isalpha()):
		name += line[i]
	elif(line[i-1].isalpha()):
		names.append(name)
		name = ''

names.sort()

scores = 0

for y in range(0, len(names)):
	scoreName = 0
	for x in range(0, len(names[y])):
		scoreName += ord(names[y][x].upper()) - 64
	scores += scoreName * (y+1)
	scoreName = 0

print(scores)

