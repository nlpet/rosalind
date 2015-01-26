from math import sqrt	

def F(n):
	return int(((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n * sqrt(5)))
	

print F(25)