# functions for repeated tasks


def read_dataset(fname):
	""" read dataset and merge all lines into a string """
	seq = ''
	f = open(fname,'r')
	seq = ''.join([line.replace('\n','') for line in f.readlines() if line[:1] != '>'])
	return seq
	

def read_dataset_multiple(fname):
	""" read dataset and append distinct strings """
	result = {}
	f = open(fname,'r')
	for line in f.readlines():
		line = line.replace('\n','')
		if line[:1] == '>':
			if not result.has_key(line): 
				k = line
				result[k] = ''
		else:
			result[k] += line
			
	return result
	
	
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