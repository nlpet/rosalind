#!/usr/bin/env python
# coding=utf-8

def get_adjacency_list(dataset):
	n = int(dataset.pop(0).replace('\n',''))
	adjacencyList = dict(zip(range(1,n+1),[[] for n in range(n)]))

	for d in dataset:
		line = [int(n) for n in d.split()]
		adjacencyList[line[0]].append(line[1])
		adjacencyList[line[1]].append(line[0])

	return adjacencyList

def traverse_subsets(k,lst,items):	
	for num in lst[k]:
		if num not in items:
			items.add(num)
			traverse_subsets(num,lst,items)
	return items


def find_interconnected_subsets(lst):
	interconnected = {}
	hub = 0
	for k,v in lst.items():
		tmp = traverse_subsets(k,lst,items=set())
		if tmp not in interconnected.values():
			interconnected['hub-'+str(hub)] = tmp
			hub += 1
	return interconnected


if __name__ == "__main__":
	dataset = open('completingATree.txt').readlines()
	subsets = find_interconnected_subsets(get_adjacency_list(dataset))
	print subsets
	print len(subsets)-1