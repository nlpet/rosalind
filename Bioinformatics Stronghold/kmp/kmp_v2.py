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

#s = 'CAGCATGGTATCACAGCAGAG'
#s = 'ABCDEFABCDE'
s = custtools.read_dataset('kmp_sample.txt')
p = [0 for _ in range(len(s))]


for i in range(1,(len(s)/2)+1):
	for j in range(i,len(s)-i+1):
		#print 'i:',i,s[:i],' j:',j,s[j:j+i]
		if s[:i] == s[j:j+i]: p[j+i-1] = len(s[j:j+i])
		
print ' '.join(str(x) for x in p)
