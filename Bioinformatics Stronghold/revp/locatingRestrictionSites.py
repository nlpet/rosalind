with open('locatingRestrictionSites.txt','r') as f:
	lines = f.readlines()
	
strings = {}
	
for l in lines:
	if l[0] == '>':
		name = l[1:].replace('\r\n','')
		strings[name] = ''
	else: 
		strings[name] += l.replace('\r\n','')

DNAComplements = {'A': 'T', 'T': 'A','G': 'C','C': 'G'}

results = {}


for k,v in strings.items():
	results[k] = {}
	for i in range(4,13):
		for j in range(0,len(v)-i+1):
			revComp =  ''.join([DNAComplements[c] for c in v[j:j+i]])[::-1]
			if v[j:j+i] == revComp: results[k][j+1] = len(revComp)
			
for k,v in results.items():
	print 'For String: ',k
	for k2,v2 in v.items():
		print k2,v2
