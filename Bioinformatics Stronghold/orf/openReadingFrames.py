import re

def read_dataset(filename):
	seq = ''
	f = open(filename,'r')
	seq = ''.join([line.replace('\n','') for line in f.readlines()[1:]])
	return seq
		
def dna_to_protein(sequence):

	codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
		
	result = ''
	
	for i in range(0,len(sequence),3):
		result += codontable[sequence[i:i+3]]
		
	return result
	
def get_reverse_complement(sequence):
	dictionary = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
	return ''.join([dictionary[char] for char in reversed(sequence)])
	
def find_sequence(sequence):
	validSequences,tmp = [],''
	p = re.compile('ATG') # START 
	
	iterator = p.finditer(sequence)
	locations = [match.span() for match in iterator]
	for loc in locations:
		tempSeq = sequence[loc[0]:]
		for i in range(0,len(tempSeq),3):
			if tempSeq[i:i+3] not in ('TAA','TGA','TAG'): tmp += tempSeq[i:i+3]
			else: 
				validSequences.append(tmp)
				tmp = ''
				break
	return validSequences
	
def get_proteins(sequence,output):
	validSequences = find_sequence(sequence)
	for vSeq in validSequences:
		output.add(dna_to_protein(vSeq))


if __name__ == '__main__':
	output = set()
	sequence = read_dataset('openReadingFrames.txt')
	reverse = get_reverse_complement(sequence)
	get_proteins(sequence,output)
	get_proteins(reverse,output)
	for o in output: print o