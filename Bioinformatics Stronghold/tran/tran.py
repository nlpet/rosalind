from __future__ import division
import custtools

ds = custtools.read_dataset_multiple('tran.txt').values()

transition, transversion = 0,0

for i in range(len(ds[0])):
	if ds[0][i] == ds[1][i]: continue
	elif ds[0][i] in ('C','T') and ds[1][i] in ('C','T'):
		transition += 1
	elif ds[0][i] in ('A','G') and ds[1][i] in ('A','G'):
		transition += 1
	else:
		transversion += 1
		

print transition / transversion