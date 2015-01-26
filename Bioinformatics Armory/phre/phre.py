from Bio import SeqIO
from numpy import mean

threshold = 27
counter = 0

for record in SeqIO.parse('phre_dataset.fastq','fastq'):
    if  mean(record.letter_annotations['phred_quality']) < threshold:
		counter += 1
    
print counter