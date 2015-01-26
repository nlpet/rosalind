import custtools
import math

dataset = custtools.read_dataset('pmch.txt')
print math.factorial(dataset.count('C')) * math.factorial(dataset.count('A'))

