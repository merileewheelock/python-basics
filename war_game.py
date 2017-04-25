#1. Thinking through steps of a program
#2. Loops!

from random import randint

cards = {
	2: "2",
	3: "3",
	4: "4",
	5: "5",
	6: "6",
	7: "7",
	8: "8",
	9: "9",
	10: "10",
	11: "Jack",
	12: "Queen",
	13: "King",
	14: "Ace"
}

suit = {
	1: "Hearts",
	2: "Diamonds",
	3: "Spades",
	4: "Clubs"
}

def user_card_drawn(user_card):
	for key,value in cards.iteritems():
		if key == user_card:
			return value

def comp_card_drawn(comp_card):
	for key,value in cards.iteritems():
		if key == comp_card:
			return value

def user_suit_drawn(card_suit):
	for key,value in suit.iteritems():
		if key == user_suit:
			return value

def comp_suit_drawn(comp_suit):
	for key,value in suit.iteritems():
		if key == comp_suit:
			return value

user_wins = 0
comp_wins = 0
ties = 0

while 1:
	user_input = raw_input("Would you like to play War? (Y/N) ")
	if user_input.upper() == "Y":
		user_card = randint(2, 14)
		comp_card = randint(2, 14)
		user_card_name = user_card_drawn(user_card)
		comp_card_name = comp_card_drawn(comp_card)
		user_suit = randint(1, 4)
		comp_suit = randint(1, 4)
		user_suit_name = user_suit_drawn(user_suit)
		comp_suit_name = comp_suit_drawn(comp_suit)
		print "You drew a {} of {} and computer drew a {} of {}.".format(user_card_name, user_suit_name, comp_card_name, comp_suit_name)
		if user_card > comp_card:
			print "You win!"
			user_wins += 1
		elif user_card < comp_card:
			print "Computer wins."
			comp_wins += 1
		elif user_card == comp_card:
			print "It's a tie!"
			ties += 1
		print "User wins: {}, Computer wins: {}, Ties: {}\n".format(user_wins, comp_wins, ties)
	else:
		print "Byeeeee"
		break