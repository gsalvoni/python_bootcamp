import random

# When defined there above, they seem to be global
suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

#########################################

class Card:
	"""Class describing the attributes of a card"""
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return "{} of {}".format(self.suit, self.rank)

class Deck:
	"""Class with the Deck attributes. The deck must be shuffled and dealt out."""
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				# Add a new card in the deck
				self.deck.append(Card(suit,rank))

	def shuffle (self):
		# Shuffle the deck
		random.shuffle(self.deck)

	def dealout (self):
		# Select the last card from the Deck
		one_card = self.deck.pop()
		return one_card

class Hand:
	"""Class showing the player's hand"""
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

class Chips:
	"""Class describing the player"""
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

########################################

def makeabet(chips):
	while True:
		try: 
			chips.bet = int(input("What is your bet?\n" ))
		except ValueError:
			print("Sorry, a bet must be an integer.")
		else:
			if chips.bet > chips.total:
				print("Sorry, your bet must be lower that your savings.")
			else:
				break

def showcards(player_hand, dealer_hand):
	print("Dealer's hand:")
	print("Hidden card")
	print("{}\n".format(dealer_hand.cards[1]))

	print("Player's hand:")
	print("{}".format(player_hand.cards[0]))
	print("{}".format(player_hand.cards[1]))
	print("Player's value: {}\n".format(player_hand.value))

def showcardsvalues(player_hand, dealer_hand):
	print("\nDealer's hand: ", *dealer_hand.cards, sep='\n')
	print("Dealer's value: ", dealer_hand.value)

	print("\nPlayer's hand: ", *player_hand.cards, sep='\n')
	print("Player's value: ", player_hand.value)

def hit(deck, hand):
	hand.add_card(deck.dealout())
	hand.adjust_for_ace()

def HitOrStand(deck, hand):
	global playing

	while True:
		inp = input("Would you like to hit or stand? Enter H or S:\n")

		if inp.upper() == 'H':
			hit(deck, hand)

		elif inp.upper() == 'S':
			playing = False 
			print("Player stands. Dealer's turn.\n")

		else:
			print("Sorry, please try again.\n")
			continue

		break

####################################### 

while True: 

	deck52 = Deck()
	deck52.shuffle()

	playerhand = Hand()
	playerhand.add_card(deck52.dealout())
	playerhand.add_card(deck52.dealout())
	playerhand.adjust_for_ace()

	dealerhand = Hand()
	dealerhand.add_card(deck52.dealout())
	dealerhand.add_card(deck52.dealout())

	playerchips = Chips()
	makeabet(playerchips)

	showcards(playerhand, dealerhand)

	while playing:

		HitOrStand(deck52, playerhand)
		showcards(playerhand, dealerhand)

		if playerhand.value > 21:
			print("You are over 21. You lose your bet!\n")
			playerchips.lose_bet()
			print("The total amount of your chips is {}\n".format(playerchips.total))
			playing = False

	if playerhand.value <= 21:

		showcardsvalues(playerhand, dealerhand)

		while dealerhand.value < 17:
			hit(deck52, dealerhand)
			showcardsvalues(playerhand, dealerhand)

		if dealerhand.value > 21:
			print("Dealer is over 21. You win your bet!\n")
			playerchips.win_bet()

		elif dealerhand.value > playerhand.value:
			print("Dealer's win. You lose your bet!\n")
			playerchips.lose_bet()

		elif dealerhand.value < playerhand.value:
			print("You win. You win your bet!\n")
			playerchips.win_bet()

		elif dealerhand.value == playerhand.value:
			print("It's a tie.\n")

		print("The total amount of your chips is {}\n".format(playerchips.total))

	newgame = input("Do you want to play another game? Y or N:\n")

	if newgame == 'N':
		print("Thank you for playing with us!")
		break
	else: 
		playing = True
		continue




