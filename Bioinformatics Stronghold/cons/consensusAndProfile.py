import operator

s = open('consensusAndProfile.txt','r')

strings = {}

with open('consensusAndProfile.txt','r') as f:
    for line in f.readlines():
        line = line.strip()
        if line[:1] == '>': 
            key = line
            strings[key] = ''
            continue
        else:
            strings[key] += line

consensus = ''
colTotal = {'A': 0, 'C': 0,'G': 0,'T': 0}
DNAStrings = {'A': [], 'C': [], 'G': [], 'T': []}

for i in range(len(strings.values()[0])):
	for j in range(len(strings)):
		colTotal[strings.values()[j][i]] += 1
	consensus += max(colTotal.iteritems(),key=operator.itemgetter(1))[0]
	for k,v in colTotal.items():
		DNAStrings[k].append(colTotal[k])
		colTotal[k] = 0
	

print consensus
for k,v in DNAStrings.items():
	print '%s: %s' % (k,' '.join([str(n) for n in v]))
