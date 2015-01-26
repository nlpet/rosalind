from Bio import ExPASy
from Bio import SwissProt

dataset = open('dbpr.txt').readlines()[0]

handle = ExPASy.get_sprot_raw(dataset) #you can give several IDs separated by commas
record = SwissProt.read(handle) # use SwissProt.parse for multiple proteins

for rec in record.cross_references:
	if rec[0] == 'GO' and rec[2][:1] == 'P': print rec[2][2:]
