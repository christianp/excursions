# Which words have unique Scrabble scores? What's the most common score? And if you replace letters with their points values, which string is most common?

alphabet = 'abcdefghijklmnopqrstuvwxyz'
tiles = {'a': 9, 'c': 2, 'b': 2, 'e': 12, 'd': 4, 'g': 3, 'f': 2, 'i': 9, 'h': 2, 'k': 1, 'j': 1, 'm': 2, 'l': 4, 'o': 8, 'n': 6, 'q': 1, 'p': 2, 's': 4, 'r': 6, 'u': 4, 't': 6, 'w': 2, 'v': 2, 'y': 2, 'x': 1, 'z': 1}
points = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2, 'f': 4, 'i': 1, 'h': 4, 'k': 5, 'j': 8, 'm': 3, 'l': 1, 'o': 1, 'n': 1, 'q': 10, 'p': 3, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 4, 'x': 8, 'z': 10}

# I downloaded the "complete word list" from http://www.scrabblejunction.org/wordlists.htm
words = open('TWL_2006_ALPHA.txt').read().split('\n')
#convert every word to lower-case
words = [word.lower() for word in words]

#decide if a word is playable
def playable(word):
	#the empty word isn't a word. Check this in case there were blank lines in the word list
	if word=='':	
		return False

	#sort the word alphabetically
	word = sorted(word)	
	i=0
	ol=None
	#walk through the word
	for l in word:	
		#if the current letter is different to the previous one,
		if l!=ol:	
			#if there were more of the previous letter than there are tiles in the bag with that letter on, this word isn't playable
			if i>tiles.get(ol,0):	
				return False
			i=1
			ol=l
		else:
			i+=1
	#check the last letter
	if i>tiles.get(ol,0):
		return False

	return True	#if none of the tests failed, this word is playable

#filter out the unplayable words
words = list(filter(playable,words))

#the score of a word is the sum of the points values of its letters
def score(word):
	return sum(points.get(l,0) for l in word.lower())

#make up a hash table associating scores to lists of words with those scores
scoredict = {}
for word in words:
	scoredict.setdefault(score(word),[]).append(word)

#find the scores that can only be obtained with one word
unique_scores = [(score,words[0]) for score,words in scoredict.items() if len(words)==1]
print('Unique scores: '+', '.join('%s (%i points)' % (word,score) for score, word in unique_scores))


# sort the scores by the number of associated words
league_table = sorted(scoredict.items(),key=lambda x:len(x[1]),reverse=True)
print('The most common score is %i points, obtained by %i words' % (league_table[0][0],len(league_table[0][1])))


#The 'score string' for a word is what you get when you replace each letter by its points score
def scorestring(word):
	return ''.join(str(points[l]) for l in word)

#make up the same kind of hash table as before, associating score strings with lists of words which produce them
ssdict = {}
for word in words:
	ssdict.setdefault(scorestring(word),[]).append(word)

#sort the score strings by how many words produce them
league_table = sorted(ssdict.items(),key=lambda x:len(x[1]),reverse=True)

print('The most common score string is %s, made by %i words' % (league_table[0][0],len(league_table[0][1])))
