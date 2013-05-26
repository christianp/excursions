from itertools import count

words = open('1-1000.txt').read().split('\n')[:-1]
primes = open('primes.txt').read().split('\n')[:-1]
primes = [int(p) for p in primes]

def factor(n):
	f = []
	if n<=1:
		return []
	for p in primes:
		if n%p==0:
			f.append(p)
		while n%p==0:
			n /= p
		if n==1:
			return f
	return f

for i in count(1):
	f = factor(i)
	if len(f):
		w = [words[primes.index(p)] for p in f]
		print(' '.join(w))
	else:
		print(i)
