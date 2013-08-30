# Find words which look like different words when the kerning of rn is bad.
# I have two word lists - one full of all sorts of nonsense, and one with just common words.
# I look for words from the big list that can look like common words, so I don't get really obtuse links like 'mirna' ~ 'mima'

words = set(w for w in open('../dictionaries/words.txt').read().split('\n')[:-1] if "'" not in w)
common_words = set(open('../dictionaries/2of12.txt').read().split('\n')[:-1])
rnwords = [w for w in words if 'rn' in w]
kemingwords = sorted([w for w in rnwords if w.replace('rn','m') in common_words])
print(', '.join(kemingwords))
