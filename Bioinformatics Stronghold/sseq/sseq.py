import re
import custtools

dataset = custtools.read_dataset_multiple('sseq.txt')
result = []
i = 0

s = max(dataset.values(),key=len)
t = min(dataset.values(),key=len)


for char in t:
	fst = s[i:].find(char) + 1
	i = fst + i
	result.append(i)
	
print ' '.join(str(r) for r in result)
