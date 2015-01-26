import urllib2
import re

# open dataset
with open('findingAProteinMotif.txt','r') as f:
	lines = f.readlines()
	
DATASET = [line.strip() for line in lines]

proteins = {}

for d in DATASET:
	response = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.fasta' % d)
	r = response.read()
	r = r.replace(re.search('>sp.+SV=\d',r).group(0),'')
	r = r.replace('\n','')
	proteins[d] = [r.find(r[i:i+4])+1 for i in xrange(len(r)-4+1) if re.search('N[^P][ST][^P]',r[i:i+4])]
	
for k,v in proteins.items():
	if v != []: print '%s\n%s' % (k,' '.join(str(n) for n in v))
