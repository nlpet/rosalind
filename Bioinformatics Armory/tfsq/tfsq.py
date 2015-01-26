from Bio import SeqIO

infile = 'tfsq_dataset.txt'
outfile = 'tfsq_dataset.fasta'

result = SeqIO.convert(infile,'fastq',outfile,'fasta')

if result: print 'Done - %s' % outfile
else:
	print 'Error'
