
def approx_pattern(substr,s,n):
   errors = sum([1 for i in range(len(substr)) if substr[i] != s[i]])
   if errors <= n: return True
   else: return False


def parse():
	f = open('1f.txt','r').readlines()
	to_find = f[0].replace('\n','')
	s = f[1].replace('\n','')
	n = int(f[2])
	indices = []
	l = len(to_find)
	
	for i in range(len(s)+1-l):
		if approx_pattern(to_find,s[i:i+l],n): indices.append(i)

	return ' '.join([str(n) for n in indices])
	
if __name__ == '__main__':
	print parse()