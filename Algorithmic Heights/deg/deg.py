
def read_graph(fname):
	info, connections = [],[]
	dataset = open('deg.txt','r').readlines()
	
	info = [int(n) for n  in dataset[0].split()]
	
	for rec in dataset[1:]:
		connections.append([int(n) for n in rec.split()])
		
	return info,connections
	
if __name__ == '__main__':
	info,connections = read_graph('deg_sample.txt')	
	output = {n+1 : 0 for n in range(info[0])}
	for n1,n2 in connections:
		output[n1] += 1
		output[n2] += 1
		
	print ' '.join([str(n) for n in output.values()])
		
	