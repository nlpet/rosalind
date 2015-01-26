DNA_CODON_TABLE = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': '-', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': '-', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': '-', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

# open dataset
with open('RNASplicing.txt','r') as f:
	lines = f.readlines()
	
c = 0
introns = []
DNAString = ''

for l in lines:
	if c > 1:
		if l[:1] == '>': c += 1
		else: introns.append(l.replace('\n',''))
	else:
		if l[:1] == '>': 
			c += 1
			continue
		else:
			DNAString += l.replace('\n','')
	
fs = ''

for i in introns:
	if DNAString.find(i) != -1: DNAString = DNAString.replace(i,'')
		
for i in range(0,len(DNAString),3):
	fs += DNA_CODON_TABLE.get(DNAString[i:i+3],'')
	
print fs

	