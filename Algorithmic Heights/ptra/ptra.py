from Bio.Seq import translate

def read_strings(fname):
	""" read dataset and append distinct strings """
	f = open(fname,'r')
	return  f.readlines()

	
if __name__ == '__main__':
	dataset = read_strings('ptra.txt')
	coding_dna = dataset[0].replace('\n','')
	result_protein = dataset[1].replace('\n','')

	protein = translate(coding_dna)
	print protein.find(result_protein) % 3 +1
	print result_protein
	print protein
