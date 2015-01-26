import itertools

with open('overlapGraphs.txt','r') as f:
	strings = f.readlines()
	
graphs = {}

k = 3

for f in strings:
	if f[0] == '>':
		name = f[1:].replace('\n','')
		graphs[name] = ''
	else:
		graphs[name] += f.replace('\n','')
		
adjacencyList = {}
perms = list(itertools.permutations(graphs.keys(),2))


for s,t in list(perms):
	if graphs[s] != graphs[t]:
		if graphs[s][-k:] == graphs[t][:k]:
			adjacencyList[s] = t
			print s,t


