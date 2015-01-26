from __future__ import division
import pdb
import random

def read_dataset(filename):
	seq,tmp = {},[]
	f = open(filename,'r')
	tmp = [line.replace('\n','') for line in f.readlines() if line[:1] != '>']
	for line in tmp:
		seq[line] = 0
	return seq
	
	
dataset = read_dataset('long.txt')

def get_all_substr(s):
	results, length = set(),len(s)
	i,k = 0,length
	while i < length/2:
		if k - i <= 5:
			k = length
			i += 1
		else:
			results.add(s[i:k])
			k -= 1
	return set(sorted(results,key=len,reverse=True))
	
def construct_superstring(s1,superstring,common):
	length_common = len(common)
	length_str = len(s1)
	if superstring.find(common) == 0:
		superstring = s1.replace(common,'') + superstring
	elif superstring.find(common) + length_common == length_str:
		superstring = superstring + s1.replace(common,'')
	return superstring
	

superstring = random.choice(dataset.keys())


while sum(dataset.values()) < len(dataset):
	for s1,v1 in dataset.items():
		if v1 == 0 and s1 != superstring:
			common = set.intersection(get_all_substr(s1),get_all_substr(superstring))
			if common != set([]):
				longest_common = max(common,key=len)
				superstring = construct_superstring(s1,superstring,longest_common)
				dataset[s1] = 1
			
print superstring
'''
def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True
'''
		