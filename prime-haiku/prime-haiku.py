# It looks like this creates haikus which evaluate to particular numbers.
# It doesn't work for every number, though it probably could.
# I have no idea when I wrote this.

from math import sqrt
import random

syllables={
	0: 1,
	1: 1,
	2: 1,
	3: 1,
	4: 1,
	5: 1,
	6: 1,
	7: 2,
	8: 1,
	9: 1,
	10: 1,
	11: 3,
	12: 1,
	13: 2,
	14: 2,
	15: 2,
	16: 2,
	17: 3,
	18: 2,
	19: 1,
}

words=['nought','one','two','three','four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

primes=[2]
biggestchecked=2
def getprime(limit):
	n=primes[-1]
	if limit>n:
		while n<=limit:
			n+=1
			top=sqrt(n)
			c=0
			isprime=1
			while primes[c]<=top and isprime:
				if n%primes[c]==0: isprime=0
				c+=1
			if isprime: primes.append(n)
	if primes.count(limit): return True
	top=sqrt(limit)
	c=0
	while primes[c]<top+1:
		if limit%primes[c]==0: return False
		c+=1
	return True

def factors(n):
	if getprime(n)==True: 
		return [n]
	else:
		f=[1]
		for prime in primes:
			while n%prime==0:
				f.append(prime)
				n//=prime
		return f

def prod(f):
	n=1
	for i in f:
		n*=i
	return n

def partitions(n):
	o=[]
	if n == 0:
		return [[]]
		
	# modify partitions of n-1 to form partitions of n
	for p in partitions(n-1):
		o+=[[1] + p]
		if p and (len(p) < 2 or p[1] > p[0]):
			o+=[[p[0] + 1] + p[1:]]
	return o
	
def haiku(n):
	lines=['','','']
	s=int(sqrt(n))
	d=n-s*s
	if d>0:
		lines[2]='plus '+haikuline(d,4)
		n=s*s
	else:
		lines[2]='times '+haikuline(s,4)
		n=s
	f=factors(n)
	if len(f)==1:
		a=int(n//2)
		b=n-a
		adds=1
	else:
		a=prod(f[:len(f)//2])
		b=prod(f[len(f)//2:])
		adds=0
	if adds:
		lines[1]='plus '
	else:
		lines[1]='times '
	lines[1]+=haikuline(b,6)
	lines[0]=haikuline(a,5)
	return '\n'.join(lines)
		
def haikuline(n,length,comeback=0):
	isprime=getprime(n)
	if n<20 or isprime:
		parts=partitions(n)
		picked=[]
		for p in parts:
			s=0
			if len([True for c in p if c in syllables])==len(p):
				for c in p: s+=syllables[c]
				s+=len(p)-1
				if s==length: picked.append(p)
	else:
		parts=factors(n)
		s=len(parts)-1
		for p in parts:
			s+=syllables[p]
		while s>length or s==0:
			parts=parts[2:]+[parts[0]*parts[1]]
			s=0
			for p in parts:
				s+=syllables[p]
			s+=len(parts)-1
		if s!=length: return mung(n,length)

	if n<20 or isprime:
		if picked != []:
			picked=random.choice(picked)
			line=words[picked[0]]+' plus '
			for c in picked[1:]:
				line+=words[c]+' plus '
			line=line[:-6]
		else:
			if comeback: return ''
			off=2
			while off<20:
				extra=haikuline(n+off,length-(1+syllables[off]),1)
				if extra=='': off+=2
				else: 
					line=extra+' less '+words[off]
					off=20
	else:
		line=words[parts[0]]+' times '
		for c in parts[1:]:
			line+=words[c]+' times '
		line=line[:-7]
	return line
	
def mung(n,length,comeback=0):
	digits=[]
	num=n
	while n>10:
		d=n%10
		digits.insert(0,d)
		n=(n-d)//10
	digits.insert(0,n)
	s=0
	line=''
	for d in digits:
		s+=syllables[d]
		line+=words[d]+'-'
	line=line[:-1]
	if comeback: return line,s
	d=length-s
	if d>0:
		end=''
		tried=[]
		ms=s+1
		while end=='' or ms>s:
			poss=[x for x in syllables.items() if (x[1]==d-1 and x[0] not in tried)]
			if len(poss)==0:
				raise "Ouch"
			off=random.choice(poss)[0]
			tried.append(off)
			end=haikuline(off,d-1,1)
			munged, ms=mung(num+off,s,1)
		line=munged+' less '+end
	if comeback: return line,s
	else: return line
	
for c in range(1,500):
	try:
		h = haiku(c)
		print('Meditation on %i:\n%s\n' % (c,h))
	except Exception:
		pass
