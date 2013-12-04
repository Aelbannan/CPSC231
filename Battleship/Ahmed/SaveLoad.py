file = open('save.apoc', 'w')
file.write('heyyyy \n')
hey = [1,2,3,4]
for i  in hey:
	file.write(str(i))
file.close()

file = open('save.apoc', 'r')
line1 = file.readline()
print(line1)
line2 = file.readline()
listi = list(line2)
for i in range(len(listi)):
	listi[i] = int(listi[i])
print(listi)
file.close()
