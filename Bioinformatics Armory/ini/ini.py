def read_dataset(fname):
	""" read dataset and merge all lines into a string """
	seq = ''
	f = open(fname,'r')
	seq = ''.join([line.replace('\n','') for line in f.readlines() if line[:1] != '>'])
	return seq
	
if __name__ == '__main__':
	from Bio.Seq import Seq
	my_seq = Seq(read_dataset('ini.txt'))
	print my_seq.count('A'),my_seq.count('C'),my_seq.count('G'),my_seq.count('T'),