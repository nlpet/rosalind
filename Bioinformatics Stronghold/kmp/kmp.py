# -*- coding: utf-8 -*-

import custtools

"""
Problem

A prefix of a length n string s is a substring s[1:j]; a suffix of s is a substring s[k:n].

The failure array of s is an array P of length n for which P[k] is the length of the longest substring s[j:k] that is
equal to some prefix s[1:k−j+1], where j cannot equal 1 (otherwise, P[k] would always equal k). By convention, P[1]=0.

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.
"""	

def find_common_substring(s, loc, j):
	c = 0

	s1 = s[:j]
	s2 = s[loc-j+1:loc+1]

	if j == 1 and s1 == s2:
		return j, c + 1

	while len(s1) > 0:
		if s2.find(s1) != -1:
			return len(s1)-1, len(s1)
		else:
			s1 = s1[:-1]
		
	return 0, 0
	
		
		
def find_failure_array(p, s, loc=1, j=1, c=0):
	"""
	:rtype : a space separated string of array p
	:param p: failure array
	:param s: string
	:param loc: location in string
	:param j: index
	:param c: count
	:return:
	"""
	if loc == len(s):
		return p, s, loc, j, c

	s1 = s[j-1:j]
	s2 = s[loc]

	if s1 == s2:
		p.append(c+1)
		find_failure_array(p, s, loc+1, j+1, c+1)
	elif c > 0 and s1 != s2:
		# find largest substring common to the prefix smaller than c
		j, c = find_common_substring(s, loc, p[-1]-1)
		p.append(c)
		find_failure_array(p, s, loc+1, j+1, c)
	else:
		p.append(c)
		find_failure_array(p, s, loc+1, j=1, c=0)

	return ' '.join([str(x) for x in p])
		
if __name__ == '__main__':
	s = custtools.read_dataset('kmp_sample.txt')
	p = [0]
	print find_failure_array(p, s)

	# 0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0