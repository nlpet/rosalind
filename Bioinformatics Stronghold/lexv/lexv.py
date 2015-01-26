from itertools import product


def read_dataset(fname):
	""" read dataset and merge all lines into a string """
	f = open(fname,'r')
	dataset = f.readline().strip().split()
	n = int(f.readline())
	return dataset,n
	
	
if __name__ == '__main__':
	dataset,n = read_dataset('lexv.txt')
	result = []
	
	result_file = open('lexv_result.txt','w')
	
	for i in range(n):
		result += list(product(dataset,repeat=i+1))
		
	for r in sorted(result,key=lambda word : [''.join(dataset).index(c) for c in word]):
		result_file.write(''.join(r)+'\n')
		
	result_file.close()
	