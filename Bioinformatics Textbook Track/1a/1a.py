
f = open('1a.txt','r').readlines()

s = f[0].replace('\n','')
l = int(f[-1])

common_strings = {}

for i in range(0,len(s)-l):
	if s[i:i+l] in common_strings.keys():
		common_strings[s[i:i+l]] += 1
	else:
		common_strings[s[i:i+l]] = 1
		
		
max_value = max(common_strings.values())
result = ''

for k,v in common_strings.items():
	if v == max_value: result += k+' '
	
print result