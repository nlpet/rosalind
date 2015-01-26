f = open('1b.txt','r').readlines()

complements = {'A': 'T','T': 'A','C': 'G','G': 'C'}

result_string = [complements[char] for char in f[0]]

print ''.join(result_string[::-1])