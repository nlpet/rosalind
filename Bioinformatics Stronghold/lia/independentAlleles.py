import time
import math



"""
Given: Two positive integers k (k=7) and N (N=2k). In this problem, we begin
with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children
in the 1st generation, each of whom has two children, and so on. Each organism
always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th
generation of Tom's family tree (don't count the Aa Bb mates at each level).
Assume that Mendel's second law holds for the factors.

probabilities = {
	'AABB': 0.063,
	'AABb': 0.125,
	'AaBB': 0.125,
	'AaBb': 0.25,
	'AAbb': 0.063,
	'Aabb': 0.125,
	'aaBB': 0.063,
	'aaBb': 0.125,
	'aabb': 0.063
}

"""

def nCk(n,k):
    f = math.factorial
    return f(n) / f(k) / f(n-k)
  
def bernoulli(n,k):
	return nCk(2**k,n) * 0.25**n * 0.75**(2**k-n)
	
def problem(k, N):
    return 1 - sum([bernoulli(n, k) for n in range(N)])


if __name__ == '__main__':
	#start_time = time.time()

	dataset = open('independentAlleles.txt').read().strip().split()
	k, N = map(int, dataset)
	print problem(k, N)
	
	#elapsed_time = time.time() - start_time
	#print("Elapsed time",elapsed_time*1000,"millisecond")
