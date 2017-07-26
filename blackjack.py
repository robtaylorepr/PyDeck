# Blackjack


class Card(object):
	RANKS = [1,2,3,4,5,6,7,8,9,10,10,10,10]
	SUITS = ['H','C','S','D']
	def __init__(self,rank,suit ):
		self.rank = rank
		self.suit = suit


class Hand(object):
    """ A hand of playing cards. """
    def __init__(self):
            self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def count(self):
    	n = 0
    	for card in self.cards:
    		n += 1
    	return n

#The Deck class is inherited from the Hand class. So it retains all #methods and attributes except for those that it overrides.
class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print ("Can't continue deal. Out of cards!" )



deck = Deck()
deck.populate()
hands = []
hands.append(Hand() )
hands.append(Hand() )
deck.deal(hands,2)
print (hands[0].count() )
print (hands[1].count() )

a = hands[0].__str__()
print (a )





