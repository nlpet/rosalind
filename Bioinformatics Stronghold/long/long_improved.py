from __future__ import division
import random
# read dataset into list
def read_dataset(filename):
    seq, tmp = [], ''
    f = open(filename,'r')
    for line in f.readlines():
        if line[:1] == '>' and tmp != '':
            seq.append(tmp)
            tmp = ''
        elif line[:1] == '>' and tmp == '': continue
        else:
            tmp += line.strip()
    seq.append(tmp) # last line
    return seq

def found_common(s1,ss):
    start,l = 0,len(s1)

    for s in range(l,int(l/2),-1):
        if ss.endswith(s1[:s]):
            return ss + s1[s:]
        elif ss.startswith(s1[start:]):
            return s1[:start] + ss
        start += 1
    return ss


if __name__ == '__main__':
    dataset = read_dataset('long.txt')
    FLAG = False
    lim = len(dataset) - 1
    ss = dataset.pop(lim)

    while len(dataset) != 0:
        for i in range(0,len(dataset)):
            newss =  found_common(dataset[i],ss)
            if len(newss) > len(ss):
                ss = newss
                dataset.pop(i)
                FLAG = True
                break
        if not FLAG:
            dataset.insert(lim,ss)
            lim -= 1
            ss = dataset.pop(lim)

    print ss
