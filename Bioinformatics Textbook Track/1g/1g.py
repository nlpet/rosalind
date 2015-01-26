import operator
from itertools import product
import time
import random
start_time = time.time()

def approx_match(substr,s,n):
	errors = sum([1 for i in range(len(substr)) if substr[i] != s[i]])
	if errors <= n: return True
	else: return False

	
def random_choice():
	f = open('1g.txt','r').readlines()
	s = f[0].replace('\n','')
	k,d = [int(nums) for nums in f[1].replace('\n','').split()]
	
	limit = len(s) * 100
	kmers = {}
	
	for i in range(limit):
		tmp = ''
		for j in range(k): tmp += random.choice(s)
			
		kmers[tmp] = 0
		for i in range(len(s)+1-k):
			if approx_match(s[i:i+k],tmp,d):
				kmers[tmp] += 1

	#print sorted(kmers.iteritems(),key=operator.itemgetter(0))
	mmax = max(kmers.values())
	return ' '.join([k for k,v in kmers.items() if v == mmax])



def find_most_common():
	f = open('1g.txt','r').readlines()
	s = f[0].replace('\n','')
	k,d = [int(nums) for nums in f[1].replace('\n','').split()]
	
	kmers = {}
	
	for p in product('ACGT',repeat=k):
		sp = ''.join(p)
		kmers[sp] = 0
		for i in range(len(s)+1):
			if approx_match(s[i:i+k],sp,d):
				kmers[sp] += 1
				
	mmax = max(kmers.values())
	return ' '.join([k for k,v in kmers.items() if v == mmax])



def parse():
	f = open('1g.txt','r').readlines()
	s = f[0].replace('\n','')
	k,d = [int(nums) for nums in f[1].replace('\n','').split()]
	
	kmers = {}
	
	for i in range(len(s)+1-k):
		s1 = s[i:i+k]
		if s1 in kmers.keys():continue
		else: kmers[s1] = 1
			
		for j in range(len(s)+1-k):
			s2 = s[j:j+k]
			if s2 == s1: continue
			if approx_match(s1,s2,d):
				kmers[s1] += 1
				
	print kmers

	mmax = max(kmers.values())
	skmers = sorted(kmers.iteritems(),key=operator.itemgetter(1))[::-1]
	for sc in skmers : print sc
	
	for i in range(k):
		to_compare = ''
		for j in range(len(skmers)):
			letter = skmers[j][0][i]+'-'+str(i)
			if letter in common.keys():
				common[letter] += 1
			else:
				common[letter] = 0
				
	print common
	print mmax
	
	hybrid = {}
	
	for k2,v in common.items():
		key = k2[:1]
		index = int(k2[-1:])
		if key in hybrid.keys(): 
			hybrid[key][index] = v
		else:
			hybrid[key] = [0] * int(k)
			hybrid[key][index] = v
	
	candidate = ''
	print hybrid
	
	for i in range(k):
		rowmax = [0,0]
		for char in ['A','C','T','G']:
			if hybrid[char][i] > rowmax[1]: rowmax[0],rowmax[1] = char,hybrid[char][i]
		candidate += rowmax[0]
		
	print candidate
	test(candidate)
	#scommon = sorted(common.iteritems(),key=operator.itemgetter(0))
	#for sc in scommon : print sc
	#return ' '.join([k for k,v in kmers.items() if v == mmax])

if __name__ == '__main__':
	#print parse()
	#print find_most_common()
	print random_choice()
	elapsed_time = time.time() - start_time
	print "Elapsed time",elapsed_time,"seconds"