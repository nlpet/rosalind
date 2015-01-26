from __future__ import division
from math import ceil,floor,log
import sys

gc_content = lambda s,l : (s.count('C') + s.count('G')) / l
at_freq = lambda x: (1 - x) / 2
gc_freq = lambda x: x / 2

def read_problem_file(fname):
	data = []
	with open(fname) as f:
		for line in f:
			data.append(line.strip().split())
	return data


if __name__ == '__main__':
	content = read_problem_file('prob.txt')
	l = len(content[0][0])
	gc_amnt = gc_content(content[0][0],l) * l
	at_amnt = l - gc_amnt

	result = []

	for c in content[1]:
		prob = float(c)
		result.append(log(gc_freq(prob)**gc_amnt * at_freq(prob)**at_amnt,10))
	
	print ' '.join(['%.3f' % x for x in result])
