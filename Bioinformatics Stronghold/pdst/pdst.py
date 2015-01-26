from __future__ import division

def read_dataset_multiple_anon(fname):
	""" read dataset and append distinct strings """
	result = []
	tmp = ''
	f = open(fname,'r')
	for line in f.readlines():
		line = line.replace('\n','')
		if line[:1] == '>':
			if tmp != '': result.append(tmp)
			tmp = ''
		else:
			tmp += line
	if tmp != '': result.append(tmp)
			
	return result
	
def hamdist(str1, str2):
	"""Count the # of differences between equal length strings str1 and str2"""
        
	diffs = 0
	for ch1, ch2 in zip(str1, str2):
		if ch1 != ch2: diffs += 1
	return diffs
	

if __name__ == '__main__':
	dataset = read_dataset_multiple_anon('pdst.txt')
	c = 0
	l = len(dataset[0])
	matrix = [[] for x in range(len(dataset))]
	for d1 in dataset:
		for d2 in dataset:
			matrix[c].append(hamdist(d1,d2)/l)
		c += 1
			
	for m in matrix:
		print ' '.join(['%.5f' % n for n in m])