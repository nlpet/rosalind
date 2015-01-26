from __future__ import division

offspring = 2

couples = [18584,16860,18916,17012,17432,16520]
     
phenotypes = ['AA-AA','AA-Aa','AA-aa','Aa-Aa','Aa-aa','aa-aa']

dominantPhenotypeProb = {'AA-AA': 1,'AA-Aa': 1,'AA-aa': 1,'Aa-Aa': 3/4,'Aa-aa': 1/2,'aa-aa': 0}

result = {}
	
for amount,phenotype in zip(couples,phenotypes):
	result[phenotype] = offspring * amount * dominantPhenotypeProb[phenotype]

print dominantPhenotypeProb
print result
print sum(result.values())

