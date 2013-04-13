# The Welsh language does not do well with the Roman alphabet.
# Similar to "fish"=="ghoti" in English, rewrite words with letters that are sometimes pronounced the same in Welsh.
# Not sure if the map below i from somewhere or completely made up.

map={
'a': ['a','ae','ya','y'],
'b': ['b','bh','by','hb'],
'c': ['c','ch','cy'],
'd': ['d','dh','th','gh'],
'e': ['e','y','f','u','i'],
'f': ['f','fh','fg','fy','yg','gh'],
'g': ['g','f','fh','th','yg','gy'],
'h': ['h','ch','gh'],
'i': ['i','y','e','u'],
'j': ['j','ch','s','gh','g'],
'k': ['ch','g'],
'l': ['l','ll'],
'm': ['m','mm',],
'n': ['n','p'],
'o': ['o','w','u','a'],
'p': ['p','pp','pf','b','bb'],
'q': ['q','c',''],
'r': ['r','rh'],
's': ['s'],
't': ['t','th','tt','d','dh'],
'u': ['w'],
'v': ['ff','fh','w'],
'w': ['w','u','w','wu'],
'x': [''],
'y': ['y','w','i'],
'z': ['z','ys'],
' ': [' ']
}


import random
def welshulate(s):
	out=''
	for letter in s:
		if letter in map:	out+=random.choice(map[letter])
		else: out+=letter
	if len(out)>2:
		c=2
		while c<len(out):
			if out[c-2]==out[c-1]==out[c]:
				out=out[:c-2]+out[c-2]*2+out[c+1:]
				c-=3
			c+=1
	return out
	
def main():
	while 1:
		print(welshulate(input()))
		
if __name__ == '__main__': main()
