#import time
#start_time = time.time()

import operator

p5 = open('computingGCContent.txt','r')
strings = {}

for line in p5.readlines():
	line = line.replace('\r\n','')
	if line[0] == '>': 
		currentString = line[1:]
		strings[currentString] = ''
	else: strings[currentString] += line
		

for k,v in strings.items():
		GCContent = v.count('C') + v.count('G')
		strings[k] = (GCContent / float(len(v))) * 100


print '\nAll:'
for k,v in strings.items(): print '%s : %.6f' % (k,v)

maxKey = max(strings.iteritems(),key=operator.itemgetter(1))
print '\nMax:\n%s\n%f' % (maxKey[0],maxKey[1])

#elapsed_time = time.time() - start_time
#print("Elapsed time",elapsed_time*1000,"millisecond")

