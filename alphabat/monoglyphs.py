import re

#test if a word uses letters at most once
def monoglyphic(word):
	word = sorted(word)
	for i in range(1,len(word)):
		if word[i]==word[i-1]:
			return False
	return True

#load words 
nonword = re.compile('[^a-z]')
words = [word.strip() for word in open('2of12.txt').readlines()]
words = [word for word in words if monoglyphic(word) and not nonword.search(word)]
f=open('monoglyphs.txt','w')
for word in words:
	f.write(word+'\n')
f.close()
