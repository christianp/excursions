# Which words can you write on a calculator?
import re

re_calc = re.compile('^[gblshezio\']+$')

words = [x.strip().lower() for x in open('words.txt').readlines()]
words = [x for x in words if re_calc.match(x)]

words.sort()
o=''
for word in words:
	o += (', ' if len(o) else '')+word
f=open('calculatorwords.txt','w')
f.write(o)
