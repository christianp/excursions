import os

def digits(n):
	d = []
	while n>0:
		m = n % 10
		d.append(m)
		n = int((n-m)/10)
	return d

got = []
graph = {}
for i in range(1000):
	while not i in got:
		got.append(i)
		t = sum([x*x for x in digits(i)],0)
		graph[i] = t
		i = t

f = open('happify.gv','w')
f.write('digraph{\noverlap=false;\nsplines=true;\n')
for i in got:
	f.write('"d%i" [label="%i"];\n' % (i,i))
for s,e in graph.items():
	f.write('d%i -> d%i;\n' % (s,e))
f.write('\n}')
f.close()
os.system('neato -Tpng happify.gv > happify.png')