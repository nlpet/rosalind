def found_common(s1,ss):
    start,l = 0,len(s1)
    i = 0
    for s in range(l,l/2,-1):
        beginning = s1[:s]
        ending = s1[i:]
        if ss.endswith(beginning):
            return ss + s1[s:]
        elif ss.startswith(ending):
            return s1[:i] + ss
        i += 1


print found_common('CCTGCCGGAA','AGACCTGCCG')