#import time
#start_time = time.time()

import operator

p5 = open('problem5.txt','r')
strings = {}

for line in p5.readlines():
	line = line.replace('\n','')
	if line[0] == '>': 
		currentString = line
		strings[currentString] = ''
	else: strings[currentString] += line
		
print '\nAll:'
for k,v in strings.items():
		GCContent = v.count('C') + v.count('G')
		strings[k] = (GCContent / float(len(v))) * 100
		
for k,v in strings.items(): print '%s : %.6f' % (k,v)

maxKey = max(strings.iteritems(),key=operator.itemgetter(1))[0]
print '\nMax:\n%s , %f' % (maxKey,strings[maxKey])

#elapsed_time = time.time() - start_time
#print("Elapsed time",elapsed_time*1000,"millisecond")

