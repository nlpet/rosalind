import math
import sys
import time
start_time = time.time()

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


# -------------------------------------------------
def read_dataset(filename):
	f = open(filename,'r')
	return [float(line.replace("\n", "")) for line in f.readlines()]


# -------------------------------------------------
def get_letter(d):
	for k,v in mimt.items():
		if math.fabs(v - d) < 5e-5: return k
	return 0
	

# -------------------------------------------------
def find_match(loc):
	for d in dataset[loc+1:]:
		match = get_letter(math.fabs(dataset[loc]-d))
		if match:
			return match,dataset.index(d)
	return 0



if __name__ == '__main__':
	dataset = read_dataset('full.txt')
	n = (len(dataset) - 3) / 2
	t = ''
	parent = dataset.pop(0)
	dataset = sorted(dataset)
	
	loc = 0
	
	while len(t) < n:
		match,loc = find_match(loc)
		if match:
			t += match
		else:
			print 'Could not find match'
			break

	print 'Output:',t
	elapsed_time = time.time() - start_time
	print "Elapsed time",elapsed_time*1000,"milliseconds"

