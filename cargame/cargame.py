# game: take the last three letters of a UK licence plate.
# Add vowels anywhere to make a word.

import re
from operator import itemgetter

#read in words
words = open('../../words.txt').read().split('\n')[:-1]

# regex matches any three letters, with any numbers of vowels interspersed
r=re.compile(r'^[aeiou]*[a-z][aeiou]*[a-z][aeiou]*[a-z][aeiou]*$')

# find words which match the regex
good_words = [w for w in words if r.match(w)]

# strip out the vowels
shorts = [(w,re.sub('[aeiou]','',w)) for w in good_words]

# I and Q are not allowed in the last three letters of a licence
shorts = [w for w in shorts if 'i' not in w and 'q' not in w]

# collect together words which come from the same three letters
plate_dict={}
for long,short in shorts:
	l=plate_dict.setdefault(short,[])
	l.append(long)

# output
print('%i endings can be made into words' % len(plate_dict.keys()))
print('%i words can be made from endings' % len(good_words))

items = list(plate_dict.items())
items.sort(key=itemgetter(0))
for short,longs in items:
	print(short)
	for long in longs:
		print('  '+long)
