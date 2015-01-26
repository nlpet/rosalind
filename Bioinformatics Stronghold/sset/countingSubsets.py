#!/usr/bin/env python
# coding=utf-8

import itertools
import operator as op
import time


start_time = time.time()

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom
        
if __name__ == "__main__":
    n,t = 984,1
    t = sum([ncr(n,k) for k in range(1,n+1)]) % 1000000
    print "Answer: %d" % t

elapsed_time = time.time() - start_time
print "Elapsed time",elapsed_time*1000,"millisecond" 