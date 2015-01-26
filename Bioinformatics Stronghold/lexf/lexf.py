from itertools import product


def read_file(filename):
	return open(filename, 'r').read().strip().split()


def print_results(info):
	n = int(info.pop())
	for p in product(info, repeat=n):
		print ''.join(p)


if __name__ == '__main__':
	print_results(read_file('lexf.txt'))





