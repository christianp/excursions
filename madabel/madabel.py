from itertools import product,combinations,count
from random import shuffle,randrange
from time import sleep

def nicelist(l):
	if len(l)<=1:
		return ''.join(l)
	else:
		return ', '.join(l[:-1])+' and '+l[-1]


class BaseCard:
	suits = ['hearts','spades','diamonds','clubs']
	sorts = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

	def __init__(self,a=0,b=0):
		self.a = a
		self.b = b

	def __eq__(c1,c2):
		return c1.a==c2.a and c1.b==c2.b

	def __hash__(self):
		return self.a*4+self.b

	def __repr__(self):
		return '%s of %s' % (self.sorts[self.a],self.suits[self.b])


def makeZCard(n):
	class Card(BaseCard):
		sorts = [BaseCard.sorts[n-1]]+BaseCard.sorts[:n-1]
		def __add__(c1,c2):
			return Card( (c1.a+c2.a) % n, (c1.b+c2.b) % 4)

		def makeDeck():
			return [Card(a,b) for a,b in product(range(n),range(4))]
	return Card

class D6Card(BaseCard):
	mult = [[0,1,2,3,4,5],[1,0,5,4,3,2],[2,4,3,0,5,1],[3,5,0,2,1,4],[4,2,1,5,0,3],[5,3,4,1,2,0]]
	sorts = [BaseCard.sorts[5]]+BaseCard.sorts[:5]
	def __add__(c1,c2):
		a = D6Card.mult[c2.a][c1.a]
		b = (c1.b+c2.b) % 4
		return D6Card(a,b)

	def makeDeck():
		return [D6Card(a,b) for a,b in product(range(6),range(4))]

class Player:
	def __init__(self,name):
		self.hand = []
		self.name = name
	
	def go(self,target,idCard):
		return []

	def __repr__(self):
		return self.name
	
class HumanPlayer(Player):
	def go(self,target,idCard):
		print('Your hand:')
		for i,c in enumerate(self.hand):
			print('%i. %s' % (i+1,c))
		inp = input('\nWhich cards do you play? ')
		if inp=='take':
			return []
		return [self.hand[int(i)-1] for i in inp.split(' ') if len(i)]

class AutoPlayer(Player):
	def go(self,target,idCard):
		for i in range(4,-1,-1):
			for cards in combinations(self.hand,i):
				if sum(cards,idCard)==target:
					return cards
		return []

class Game:
	def __init__(self,Card,reporting=True):
		self.reporting = reporting
	
		self.Card = Card
		self.idCard = Card()

		self.deck = Card.makeDeck()
		shuffle(self.deck)

		self.pile = []

		self.play(self.deal(2))	#deal two cards onto the pile

		self.players = []
	
	def addPlayers(self,*players):
		for player in players:
			self.players.append(player)
			player.hand = self.deal(7)

	def deal(self,n):
		if len(self.deck)<n:
			top = self.pile[-2:]
			bottom = self.pile[:-2]
			bottom.reverse()
			self.deck = bottom + self.deck
		b=self.deck[-n:]
		del self.deck[-n:]
		return b

	def play(self,cards):
		self.pile += cards
		self.target = sum(self.pile[-2:],self.idCard)

	def report(self,msg,delay=0.2):
		if self.reporting:
			print(msg)
			sleep(delay)
	
	def describeTarget(self):
		self.report('The %s and the %s are on the top of the pile.' % (self.pile[-1],self.pile[-2]))

	def run(self):
		start = randrange(len(self.players))
		for i in count():
			player = self.players[(i+start) % len(self.players)]
			self.report("Turn %i. %s's go." % (i+1,player))
			self.describeTarget()

			cards = player.go(self.target,self.idCard)
			while len(cards)>0 and sum(cards,self.idCard)!=self.target:
				self.report("\nThose cards don't sum to the target. Try again.")
				self.describeTarget()
				cards = player.go(self.target,self.idCard)

			if len(cards)==0:
				self.report('^^ %s draws two cards from the deck' % player)
				player.hand += self.deal(2)
			else:
				self.report('>> %s plays %s' % (player, nicelist(['the '+str(c) for c in cards])))
				self.play(cards)

				player.hand = [c for c in player.hand if not c in cards]
				if len(player.hand)==0:
					self.report('!! %s has no cards left!\n\n%s wins!' % (player,player))
					return player
			self.report('\n',1)

def demo():
	#size=int(input("How many cards per suit? "))
	game = Game(Card=D6Card)
	game.addPlayers(
		AutoPlayer('Bot'),
		HumanPlayer(input('What is your name? '))
		)
	game.run()

if __name__ == '__main__':
	demo()
