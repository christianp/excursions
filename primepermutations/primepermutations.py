# Find three-digit primes where any reordering of the digits is still prime.

#generate a list of primes, somewhat inefficiently
primes=[2]
for x in range(3,999,2):
	if len([y for y in primes if y*y<=x and x % y == 0])==0:
		primes.append(x)

#keep only three-digit primes
primes = [x for x in primes if x>100]

#collect primes into anagram classes
k={}
for p in primes:
	#convert number to a string then a list, sort it, convert back to string then int
	x=int(''.join(sorted(list(str(p)))))
	#add this number to the list of numbers anagrammatically equivalent
	k[x] = k.get(x,[])+[p]

#now k[x] contains all the prime anagrams of x

#sort the classes of anagrams by length
scores=sorted(k.values(),key=len)
for x in scores:
	print(x)
