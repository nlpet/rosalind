from Bio import Entrez

term = 'Clito'
datetype = 'pdat'
mindate = '2010/11/05'
maxdate = '2012/08/31'


Entrez.email = "np@axion.me.uk"
handle = Entrez.esearch(db="nucleotide", term='"%s"[Organism] AND ("%s"[%s] : "%s"[%s]' % (term,mindate,datetype.upper(),maxdate,datetype.upper()))
record = Entrez.read(handle)
print record["Count"]

