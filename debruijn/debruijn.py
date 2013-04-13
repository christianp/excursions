# de Bruijn card trick computatorator
# by Christian Perfect
# based on a trick by Persi Diaconis and Ron Graham

#names of cards
faces = ['King','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen']
suits = ['Diamonds','Clubs','Hearts','Spades']

#generate de bruijn sequence
sequence = [0,0,0,0,0,1]
for i in range(6,64):
	sequence.append( (sequence[i-6]+sequence[i-5]) % 2 )

#get a string of binary digits representing an integer
def binarise(n,length):
	digits=[]
	while n>0:
		digits.insert(0,int(n%2))
		n=(n-n%2)/2
	digits = [0]*(length-len(digits))+digits	#pad to the desired length
	return digits

#decode a string of binary digits to an integer
def debinarise(digits):
	n=0
	for i in digits:
		n*=2
		n+=i
	return n

#decode a six-digit binary string to a card
def decode_sequence(seq):
	number = debinarise(seq[:4])
	suit = debinarise(seq[4:])
	return number,suit

#turn a card into a six-digit binary string
def encode_card(card):
	number,suit = card
	return ''.join([str(x) for x in binarise(number,4)+binarise(suit,2)])

#display a card's binary encoding and its name
def show_card(card):
	number,suit = card
	return '%s: %s of %s' % (encode_card(card), faces[number], suits[suit])


# The actual computation!
sequence*=2	#take two copies of the sequence to cope with the cycle at the end

# Get the ordering of the (64, not all real) cards from the sequence
cards = [decode_sequence(sequence[i:i+6]) for i in range(0,64)]

# The deck of cards consists of the first 52
deck = cards[:52]

# Get the unused cards from the end of the 64-deck which have usable values
castoffs = [(x,y) for (x,y) in cards[52:] if x<13]
# Separate them into red and black
castoffs_red = [(x,y) for (x,y) in castoffs if y%2==0]
castoffs_black = [(x,y) for (x,y) in castoffs if y%2==1]

# Get the cards from the 52-deck that don't have usable values
toswap = [(x,y) for (x,y) in deck if x>=13]
swaps = {}

# Match up bad cards in the 52-deck with good cards in the castoffs
for card in toswap:
	number,suit = card
	b=castoffs_red.pop() if suit%2==0 else castoffs_black.pop()
	swaps[card]=b

# Show the resulting ordering of the real 52-card deck
for i in range(0,52):
	digits = sequence[i:i+6]
	card = decode_sequence(digits)
	if card in swaps.keys():
		card = swaps[card]
	print(show_card(card))

# Show which bad codes are swapped with which good ones
print('Swaps')
for a,b in swaps.items():
	print('%s -> %s' % (encode_card(a),show_card(b)))
