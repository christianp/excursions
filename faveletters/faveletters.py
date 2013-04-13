from re import compile
from operator import itemgetter
from math import sqrt

words = [x.strip() for x in open('2of12.txt').readlines()]	#load in my list of words

def top(letter):
#returns the letter's favourite words - those which contain that letter the most times
	r=compile('[^%s]' % letter)	#regular expression to match everything that isn't the letter we want
	scoreboard = [(word,len(r.sub('',word))) for word in words]	#for each word, work out how many times it contains the wanted letter by stripping out all other letters
	scoreboard.sort(key=itemgetter(1),reverse=True)	#sort by score
	topscore = scoreboard[0][1]	#the score of the word at the start of the list is the top score
	topscoreboard = [word for word,score in scoreboard if score==topscore]	#get all words with the same score (this could be quicker, but list comprehensions are so easy!)
	return (topscore,topscoreboard)	#return the top score and the words with that score

#print out the top scores and words for each letter in the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:	
	score,lwords = top(letter)
	print('%s (%i): %s' % (letter,score,', '.join(lwords)))
