

def find_longest_ending_in_n(n,tmp,mode):
	if mode == 'inc':
		longest = [lst for lst in tmp if lst[-1] < n]
	elif mode == 'dec':
		longest = [lst for lst in tmp if lst[-1] > n]
	if longest != []: return max(longest,key=len)
	else: return None
	
def traverse(arr,tmp,mode):
	for n in range(1,len(arr)): 
		longest = find_longest_ending_in_n(arr[n],tmp,mode)
		if longest:
			tmp.append(longest + [arr[n]])
		else: tmp.append([arr[n]])
	
	return tmp

if __name__ == '__main__':
	dataset = open('longestIncreasingSubsequence.txt','r').readlines()
	arr = [int(n) for n in dataset[1].split(' ')]

	tmpinc = [[arr[0]]]
	tmpdec = [[arr[0]]]
	
	longest_inc = max(traverse(arr,tmpinc,'inc'),key=len)
	longest_dec = max(traverse(arr,tmpdec,'dec'),key=len)
	print ' '.join([str(n) for n in longest_inc])
	print ' '.join([str(n) for n in longest_dec])