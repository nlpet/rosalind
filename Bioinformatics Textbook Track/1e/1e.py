import re
import time
	
def skew():
	f = open('1e.txt','r').readlines()
	s= f[0].replace('\n','')
	total = 0
	result = [0]
	
	for i in range(len(s)):
		if s[i] == 'C': total -= 1
		elif s[i] == 'G': total += 1
		result.append(total)

	mmin = min(result)
	return ' '.join([str(i) for i in range(len(result)) if result[i] == mmin])
	
def min_skew():
	f = open('1e.txt','r').readlines()
	s= f[0].replace('\n','')
	total = 0
	min_skew = 0
	indices = []
	
	for i in range(len(s)):
		if s[i] == 'C': total -=1
		elif s[i] == 'G': total +=1
		
		if total < min_skew:
			min_skew = total
			indices = [i+1]
		elif total == min_skew and s[i] not in indices:
			indices.append(i+1)
	
	return ' '.join([str(n) for n in indices])
	
if __name__ == '__main__':
	start_time = time.time()
	#print skew()	
	print min_skew()
	
	elapsed_time = time.time() - start_time
	print "Elapsed time",elapsed_time*1000,"milliseconds"