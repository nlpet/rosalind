import string

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
	

def find_longest_ending_in_n(n,tmp):
	longest = [lst for lst in tmp if lst[-1] <= n]
	if longest != []: return max(longest,key=len)
	else: return None
	
def traverse(arr,tmp):
	for n in range(1,len(arr)): 
		longest = find_longest_ending_in_n(arr[n],tmp)
		if longest:
			tmp.append(longest + [arr[n]])
		else: tmp.append([arr[n]])
	
	return tmp

if __name__ == '__main__':
	dataset = read_dataset_multiple_anon('lcsq_sample.txt')
	
	d1 = [string.ascii_uppercase.index(x) for x in dataset[0]]
	print dataset[0],'',d1
	#tmpinc = [[d1[0]]]
	#longest_inc = max(traverse(d1,tmpinc),key=len)
	#print ' '.join([str(n) for n in longest_inc])
	
	d2 = [string.ascii_uppercase.index(x) for x in dataset[1]]
	print dataset[1],d2
	#tmpinc = [[d2[0]]]
	#longest_inc = max(traverse(d2,tmpinc),key=len)
	#print ' '.join([str(n) for n in longest_inc])
