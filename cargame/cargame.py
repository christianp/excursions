# game: take the last three letters of a UK licence plate.
# Add vowels anywhere to make a word.

import re
from operator import itemgetter

words = open('words.txt').read().split('\n')[:-1]

words = [w for w in words if "'" not in w]

r=re.compile(r'^[aeiou]*[a-z][aeiou]*[a-z][aeiou]*[a-z][aeiou]*$')

good_words = [w for w in words if r.match(w)]

shorts = [(w,re.sub('[aeiou]','',w)) for w in good_words]

plate_dict={}
for long,short in shorts:
	l=plate_dict.setdefault(short,[])
	l.append(long)

print('%i endings can be made into words' % len(plate_dict.keys()))
print('%i words can be made from endings' % len(good_words))

items = list(plate_dict.items())
items.sort(key=itemgetter(0))
for short,longs in items:
	print(short)
	for long in longs:
		print('  '+long)
