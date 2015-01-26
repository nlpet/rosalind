#import time
#start_time = time.time()

def rabbits(n,k):
	gen = 1
	a,b = 1,1
	while (gen<=n-2):
		a,b = a+k*b,a
		gen += 1
	return a
	
print rabbits(29,2)


#elapsed_time = time.time() - start_time
#print("Elapsed time",elapsed_time*1000,"millisecond")