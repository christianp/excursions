# find pairs of petrol prices and litres of petrol such that the amount you pay, as well as the price to 1 dp and the amount to 2 dp, are all palindromes
# the ranges of prices and volumes are quite restricted to only get "reasonable" values.
 
from itertools import product,tee
 
def palindromes():
  #palindrome generator
  #this algorithm ends up using lots of memory!
	a=[0,1,2,3,4,5,6,7,8,9]
	b=[00,11,22,33,44,55,66,77,88,99]
	t=100
	while True:
		for i in a:
			yield i
		na = []
		for i in range(1,10):
			na+=[t*i+c*10+i for c in a]
		a,b=b,na
		t = t*10
 
ps=[]
for i in palindromes():
	if i>100:
		ps.append(i)
	if i>9999999:
		break
pset=set(ps)
 
def ordered_pairs(l):
	for i in range(len(l)):
		a=l[i]
		for b in l[i:]:
			yield (a,b)
 
for a,b in ordered_pairs(ps):
	if a<10000 and b<10000:
		prod=round(a*b/1000)
		if prod in pset:
			print('%.1f*%.2f = %.2f' % (a/10,b/100,prod/100))