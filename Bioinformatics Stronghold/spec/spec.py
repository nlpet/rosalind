import math

mimt = {
	"A":  71.03711,
	"C":  103.00919,
	"D":  115.02694,
	"E":  129.04259,
	"F":  147.06841,
	"G":  57.02146,
	"H":  137.05891,
	"I":  113.08406,
	"K":  128.09496,
	"L":  113.08406,
	"M":  131.04049,
	"N":  114.04293,
	"P":  97.05276,
	"Q":  128.05858,
	"R":  156.10111,
	"S":  87.03203,
	"T":  101.04768,
	"V":  99.06841,
	"W":  186.07931,
	"Y":  163.06333
}

def read_dataset(filename):
	l = []
	f = open(filename,'r')
	l = [float(line.replace('\n','')) for line in f.readlines()]
	return l

def uncover_protein(dataset):
	closest = ''
	for i in range(len(dataset)-1):
		diff = dataset[i+1] - dataset[i]
		closest += [k for k,v in mimt.items() if math.fabs(diff - v) < 5e-5][0]
	return closest
	
if __name__ == '__main__':
	dataset = read_dataset('spec.txt')
	print uncover_protein(dataset)