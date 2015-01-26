import time
start_time = time.time()

with open('findingASharedMorif.txt','r') as f:
	lines = f.readlines()
	
s = {}

c,strings = -1,['']*sum([1 for l in lines if l[0] == '>'])
for l in lines:
	if l[0] == '>': c += 1
	else: strings[c] += l.replace('\n','')
		

shortest = min(strings)
strings.remove(shortest)

results = []

l = len(shortest)

for i in range(l):
	for j in range(l,i+1,-1):
		if sum([1 for s in strings if s.find(shortest[i:j]) != -1]) == len(strings): 
			results.append(shortest[i:j])

print max(results,key=len)

elapsed_time = time.time() - start_time
print "Elapsed time",elapsed_time*1000,"milliseconds"