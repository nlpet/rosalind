from itertools import permutations
from math import fabs
import time

start_time = time.time()

r = []
n = 6


for p in permutations([x for x in range(-n,n+1) if x != 0],n):
    if len(p) == len(set([fabs(n) for n in p])): r.append(p)
	
	
result_file = 'sign_result.txt'
result = open(result_file,'w')

# write results to file
result.write(str(len(r))+'\n')
for t in r:
	result.write(' '.join([str(t1) for t1 in t])+'\n')
	
result.close()

# print stats
print 'Done - %s' % result_file
elapsed_time = time.time() - start_time
print "Elapsed time",elapsed_time*1000,"milliseconds" 