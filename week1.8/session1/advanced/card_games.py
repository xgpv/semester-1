# In this file, you have two classes, Card and Deck.

# Both have been set up with some basic methods (constructors, and a couple of dunder methods)

# Deck has two methods which need completing - shuffle and deal.

# With these methods, you should be able to create almost any card game which you can think of!

# We recommend having a go at implementing one of:
# - snap (easiest)
# - blackjack (easy scoring)
# - baccarat (slightly harder scoring)
# - poker (more difficult)

# If you have another card game you want to implement - go for it!

# You can edit/add to/change these classes as you need to.


import random
import sys


class Card:
    """
    Class to represent a single playing card.
    """

    def __init__(self, rank, suit):
        """
        Creates a playing card with the given rank & suit.
        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    """
    Class to represent a deck of playing cards.
    """

    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

    RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        """
        Creates a full deck of cards.
        """
        self.deck = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        """Shuffles this deck randomly."""
        # NEEDS COMPLETING
        return random.shuffle(self.deck)

    def deal(self):
        """Removes top card from this deck and returns it."""
        # NEEDS COMPLETING
        card = self.deck[0]
        self.deck.pop(0)
        return card
    
    def handview(self, hand, handd):
        print(f"Your hand: {', '.join(str(card) for card in hand)}\nValue: {deck.rankvalues(hand)}\nDealer's hand: {', '.join(str(card) for card in handd)}\nValue: {deck.rankvalues(handd)}\n")

    def rankvalues(self, hand):
        """Takes the rank of a hand and returns its value"""
        rankvalues = {rank: value for value,rank in enumerate(Deck.RANKS, start=2)}
        rankvalues['Jack'] = 10
        rankvalues['Queen'] = 10
        rankvalues['King'] = 10
        rankvalues['Ace'] = 11
        total = 0
        for card in hand:
            total += int(rankvalues[card.rank])
        return total
    
    def choice(self, hand, choice):
        """Details the choices the user has"""
        if choice == 's':
            hand.stand()
        elif choice == 'h':
            yourhand.append(Deck.deal(deck))
            deck.handview(yourhand, dealerhand)
            hand.check()
        else:
            print('Error')
        return choice
    
    def hit(self, hand):
        yourhand.append(Deck.deal(deck))

        

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return "\n".join(str(c) for c in self.deck)


# Implement a card game!
print("Let's play Blackjack!|\n")
deck = Deck()   # Initialises the variables to start the game
Deck.shuffle(deck)
yourhand = []
dealerhand = []
for i in range(2):   # Deals two cards to dealer and player
    yourhand.append(Deck.deal(deck))
    dealerhand.append(Deck.deal(deck))


deck.handview(yourhand, dealerhand) 
cond = True
while cond:
    choice = input('Next move?\nHit - Type: h\nStand - Type: s\n').strip().lower()
    if choice not in {'h', 's'}:
        print('Enter a valid choice\n')
    else:
        cond = False
choice = deck.choice(yourhand, choice)
#while choice != 's':
