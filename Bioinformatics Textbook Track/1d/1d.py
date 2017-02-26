import re
import time
	
def find_kmers():
	f = open('1d.txt','r').readlines()

	s= f[0].replace('\n','')
	k,L,t = [int(n) for n in f[1].split()]

	results = {}
	kmers = []

	for i in range(len(s)-k+1):
		indices = [m.start()+1 for m in re.finditer(s[i:i+k], s)]
		if indices >= t: 
			results[s[i:i+k]] = indices

	for key,v in results.items():
		for i in range(len(v)-t+1):
			if ((v[i+t-1]+k) - v[i] <= L) and (key not in kmers): kmers.append(key)

	return ' '.join(kmers)

	
	
if __name__ == '__main__':
	start_time = time.time()
	print find_kmers()
	elapsed_time = time.time() - start_time
	print "Elapsed time",elapsed_time*1000,"milliseconds"
