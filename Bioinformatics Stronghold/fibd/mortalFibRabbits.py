import time
start_time = time.time()

n,m = 85,19

rabbits = [1] + [0]*m

total,babies = 0,0

for month in xrange(1,n):
	for i in xrange(len(rabbits)-1,0,-1):
		if rabbits[i-1] == 0: continue
		rabbits[i] += rabbits[i-1]
		rabbits[i-1] = 0
	rabbits[0] = babies
	if rabbits[-1] != 0: rabbits[-1] = 0 # killing rabbits
	babies = sum(rabbits[1:])
	
print 'Total: %d ' % sum(rabbits)

elapsed_time = time.time() - start_time
print "Elapsed time",elapsed_time*1000,"millisecond"

# FASTER ALGORITHM
'''
#!/usr/bin/env python
def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in xrange(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)

print fib(85,19)
'''