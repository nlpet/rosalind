from Bio import Entrez
from Bio import SeqIO


dataset = open('frmt.txt','r').readlines()
Entrez.email = "np@axion.me.uk"
handle = Entrez.efetch(db="nucleotide", id=dataset, rettype="fasta")
records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format

shortest = {'description': '', 'seq': '', 'len': 9999}

for r in records:
	if len(r.seq) < shortest['len']:
		shortest['description'] = r.description
		shortest['seq'] = r.seq
		shortest['len'] = len(r.seq)
		

print '>' + shortest['description']
print shortest['seq']
print shortest['len']