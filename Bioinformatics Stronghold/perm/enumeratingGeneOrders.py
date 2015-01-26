import itertools

n = 6

f = open('enumeratingGeneOrders.txt','w')

perms = list(itertools.permutations(range(1,n+1)))
f.write(str(len(perms))+'\n')

[f.write(' '.join([str(n) for n in p])+'\n') for p in perms]

f.close()