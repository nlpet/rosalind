import time
start_time = time.time()

import collections

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

def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]
	
common = []
for s in strings:
	common.append(longest_common_substring(s,shortest))
	

print [x for x, y in collections.Counter(common).items() if y >= 1]

elapsed_time = time.time() - start_time
print "Elapsed time",elapsed_time*1000,"milliseconds"