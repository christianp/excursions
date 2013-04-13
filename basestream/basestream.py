import sys
from itertools import count,islice
from random import randint

from math import sqrt	#needed for standard deviation calculation, not for the number stream, before you get worried

def debug(t):
	return  #comment this line out if you want the running of the algorithm to be narrated
	print(t)

#take n values from generator gen
def take(gen,n):
	return list(islice(gen,n))

#generate the bases for the accumulators
#yields tuples (b,k), where the base of the accumulator is b**k
#so we need to accumulate k base-b digits before we can yield something
def make_accsgen(n):
	b=2
	k=1
	c=b
	accs = []

	while b>1:
		while c<n:
			k+=1
			c*=b
		yield (b,k)
		b = c-n
		k=1
		c=b

#infinite stream of binary digits
binstream = (randint(0,1) for x in count())

#multiply out digits in given base to an integer
def prod(digits,base):
	n=0
	for digit in digits:
		n*=base
		n+=digit
	return n

#generates a uniform random stream of digits in given base
def uniformstream(base,binstream=binstream):
	accsgen = make_accsgen(base)	#genrator for accumulators
	b2,k2 = next(accsgen)	#b2 is always 2. k2 is least number such that 2**k2>=
	accbases=[]	#this will store bases and numbers of digits for the accumulators
	accs=[]	#list of lists of digits for each accumulator

	while True:
		n=0
		for i in range(k2):	#take k2 binary digits
			n*=2
			try:
				n+=next(binstream)
			except StopIteration:
				raise
		debug('picked %i from binary stream' % n)

		b,k=b2,k2

		#the idea:
		#got a stream of base-b digits, want to convert to a stream of base-c digits
		#pick least number b^k which is greater than c
		#generate numbers in range 0..b^k-1
		#if generated number is less than c, keep it
		#otherwise, throw it away
		#but don't throw it away!
		#keep it, and use it to start a stream of base (b^k-c) digits
		#and do the same thing with that stream

		while n>=base:
			debug('n too big: %i' % n)
			n -= base
			debug('n := %i' %n)
			if i==len(accs):
				try:
					accs.append([])
					accbases.append(next(accsgen))
				except StopIteration:
					accbases.append((base+1,1))
					n=-1
					debug('too big')
					break
				debug('need another accumulator: %i**%i' % accbases[-1])
			b,k = accbases[i]
			if b**k==base+1:	#if the base of this accumulator is just one more than the base we want, we can't do anything with the remainder so have to throw this number away
				debug('whoops')
				n=-1
				break
			accs[i].append(n)
			debug('base %i accumulator: %s' % (b**k,accs[i]))
			if len(accs[i])==k:
				n=prod(accs[i],b)
				accs[i]=[]
				debug('accumulator yielded %i' % n)
			else:
				n=-1
			i+=1

		if n>=0:
			debug('YIELD %i' % n)
			yield n

if __name__ == '__main__':
	#DEMO!

	n=int(sys.argv[1])
	print('generating numbers base %i' % n)

	s=uniformstream(n)	#create stream generator

	print('10 samples: %s' % take(s,10))

	freq = [0 for i in range(n)]
	samples = 10000
	print('Now generating %i samples' % samples)
	for i in take(s,samples):
		freq[i]+=1

	#display frequency table
	for i,f in zip(range(n),freq):
		print('%i occurred %i times' % (i,f))

	#calculate summary statistics of frequency counts
	#if sample mean == samples/n, then generator is uniform
	mean = sum([i*x for i,x in zip(count(),freq)])/samples
	print('mean: %f (should be %f)' % (mean,(n-1)/2))
	stddev = sqrt(sum([freq[x]*(x-mean)**2/samples for x in range(0,n)]))
	print('standard dev: %f' % stddev)
