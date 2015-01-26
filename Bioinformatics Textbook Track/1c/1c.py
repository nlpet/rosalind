
f = open('1c.txt','r').readlines()

to_find = f[0].replace('\n','')
string = f[1].replace('\n','')


l = len(to_find)
indices = []

for i in range(len(string)-l+1):
	if string[i:i+l] == to_find: indices.append(i)
	
print ' '.join([str(n) for n in indices])
