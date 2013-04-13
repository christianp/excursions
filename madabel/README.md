A python3 version of the game Mad Abel (http://www.pagat.com/docs/madabel.pdf)

The rules:

From a deck of cards, take those numbered ace to N of all four suits, and throw the rest away.
Deal 4 cards to each player, and two cards face-up in a pile on the table. Put the rest of the deck face-down on the table.

This is a game based on adding cards together.

The sum of a set of cards is:

the sum of the face values (modulo N)
the sum of the suits (modulo 4)
The suits have the following values:

hearts - 0
spades - 1
diamonds - 2
clubs - 3
So in the game where face values go up to 5, the sum of the 3 of diamonds and the 4 of clubs is the 2 of spades.

The target is the sum of the top two cards on the pile. Players take turns to make up the sum using any combination of the cards in their hands. If a player can't make the target, they draw two cards from the deck and the next player takes their turn.

The winner is the first person to get rid of all their cards.

