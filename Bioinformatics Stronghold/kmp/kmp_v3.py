# -*- coding: utf-8 -*-

import custtools
import sys

"""
Problem

A prefix of a length n string s is a substring s[1:j]; a suffix of s is a substring s[k:n].

The failure array of s is an array P of length n for which P[k] is the length of the longest substring s[j:k] that is
equal to some prefix s[1:k−j+1], where j cannot equal 1 (otherwise, P[k] would always equal k). By convention, P[1]=0.

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.
"""


def loop_through(lst, s, p, ind):
	""" loop through lst at index n and compare n to ind """
	tmp = []
	for n in lst:
		if n >= len(s): return [], s, p, ind+1
		if s[n] == s[ind] and n != ind:
			p[n] = ind+1
			if n+1 < len(s): tmp.append(n+1)

	return tmp, s, p, ind+1


def start():
	#s = 'CAGCATGGTATCACAGCAGAG'

	s = custtools.read_dataset('kmp.txt')
	p = [0 for _ in range(len(s))]
	
	temp = []
	for j in range(1,len(s)):
		if s[j] == s[0]:
			if j+1 < len(s):
				temp.append(j+1)
			p[j] = 1

	i = 1

	while 1:
		temp, s, p, i = loop_through(temp, s, p, i)
		if not temp:
			break

	print ' '.join(str(x) for x in p)

# -------------------------------
if __name__ == '__main__':
	start()


