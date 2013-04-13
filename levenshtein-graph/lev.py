from itertools import combinations

def lev(s1, s2):	#from wikibooks: http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
    s1,s2=[x.lower() for x in (s1,s2)]
    if len(s1) < len(s2):
        return lev(s2, s1)
    if not s1:
        return len(s2)
 
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]

def levgraph(names):
	dist = [(lev(x,y),x,y) for x,y in combinations(names,2)]
	dist.sort(key=lambda x:x[0])
	got=set()
	edges=[]
	while(len(got)<len(names)):
		d,x,y = dist[0]
		got.update((x,y))
		edges.append((d,x,y))
		dist=[(d,x,y) for d,x,y in dist if x not in got or y not in got]
	return edges

if __name__ == '__main__':
	names=['Stacey Aston','Nathan Barker','Matthew Buckley','David Elliott','Michael Garrett','Christian Perfect','Daniel Wacks']
	edges = levgraph(names)
	f=open('lev.gv','w')
	f.write('graph PHD2 {\n\tratio=0.55;fontname="Calibri";fontsize=24;label="PHD2";size="5.374,4.5";margin=0;\n\n\tnode [shape=none,fontname="Calibri",fontsize=20];\n')
	[f.write('\t"%s";\n' % x) for x in names]
	f.write('\n')
	[f.write('\t"%s" -- "%s" [len=%f,label=%i];\n' % (x,y,d*.15,d)) for d,x,y in edges]
	f.write('}')
	f.close()
	print('\n'.join('%i %s, %s' % edge for edge in edges))
