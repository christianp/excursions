#top fact: loads of words starting with 'gr' are still words if you change the 'gr' to 'h'
#eg grip -> hip, grand -> hand, grow -> how, etc.
#which prefix-swapping pair has the most congruences?

def computeprefixpairs():
	#load in all the words of three letters or more
	words = [word for word in open('words.txt').readlines() if len(word)>3]

	#the keys of splits are suffixes and the values are lists of prefixes such that prefix+suffix = a real word
	#so for each suffix, we will be able to get a list of all the prefixes you can stick in front of it to get a real word
	splits={}

	#count, for each pair of prefixes, how many words remain valid when you swap one prefix for another
	pairs={}

	pairsuffixes={}

	for word in words: #for each word in the list:
		for i in [1,2]:	#take the prefixes of length 1 and 2
			prefix=word[:i]	#get the prefix
			suffix=word[i:]	#get the rest of the word

			if suffix in splits:
				#each prefix already found for this suffix can be swapped with the new prefix
				#so add one to the counter for the pair (new prefix, old prefix)
				for oprefix in splits[suffix]:
					p1,p2 = min(prefix,oprefix), max(prefix,oprefix)
					pairs[p1,p2] = pairs.get((p1,p2),0) + 1
					pairsuffixes[p1,p2]=pairsuffixes.get((p1,p2),[])
					pairsuffixes[p1,p2].append(suffix)

				#add the new prefix to the list of found prefixes which go with this suffix
				splits.get(suffix,[]).append(prefix)
			else:
				splits[suffix]=[prefix]

	winners = sorted(pairs.items(),key=lambda x:x[1],reverse=True)

	#return: 
	#	the list of prefix-pairs, sorted by how many suffixes they have in common
	#	the dictionary matching up suffixes with prefixes
	return (winners,splits,pairsuffixes)

if __name__ == '__main__':
	winners,splits,pairsuffixes = computeprefixpairs()
	result = '\n'.join([x[0][0]+'\t'+x[0][1]+'\t'+str(x[1]) for x in winners])
	open('prefixchange.txt','w').write(result)
	print("Results written to prefixchange.txt")
