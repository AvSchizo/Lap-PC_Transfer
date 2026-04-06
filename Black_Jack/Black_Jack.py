import random
import math
import time

# dealer wait time
dWT = 1.5

# win sleep time
bWT = 1.5

Ranks = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')
Tens = (10, 'Jack', 'Queen', 'King')

def newDeck():

	tempDeck = []

	for i in range(4):

		for i in range(13):
			tempDeck.append(Ranks[i])
	
	return tempDeck


def Shuffle(deck):
	deck = random.shuffle(deck)

def recycle():
	deck = newDeck()
	Shuffle(deck)
	return deck


def Bet(money):

	while True:

		print(f"Money: {money}")
		bet = input("Bet: ")

		if bet.isdigit():
			bet = int(bet)

			if bet <= money:
				print()
				return bet
		
		elif bet == "quit":
			return "quit"
		
		else:
			print("Sorry, I don't understand")
			print()


def findTotal(hand):
	total = 0
	# finds total
	for i in range(len(hand)):
		cardCheck = hand[i]

		if cardCheck in Tens:
			total += 10
		elif cardCheck == "Ace":
			total += 11
		else:
			total += cardCheck
	
	# condences aces if necessary
	for i in range(len(hand)):
		if hand[i] == 'Ace' and total > 21:
			total -= 10
	
	return total


def hit(hand, deck):
	print(f"The dealer deals {deck[0]}")
	hand.append(deck.pop(0))


def printCards(char):
	if char == dealer:
		print(f"Dealer's cards: {char.hand}")
	else:
		print(f"Player's cards: {char.hand}")
	print(f"Total: {char.total}")





class playerChar():
	def __init__(self, money):
		self.money = money



Deck = newDeck()

p = playerChar(200)
dealer = playerChar(10000)


# making sure game loop goes into menu loop
while True:
	# menu loop
	while True:
		print()
		print("MAIN MENU")
		print()

		menuChoice = input("(start)/(quit): ")

		if menuChoice == "start":
			print()
			break
		elif menuChoice == "quit":
			quit()
		else:
			print("Sorry, I don't understand")

	# round loop
	while True:

		menu = False
		winner = "none"
		Deck = recycle()

		bet = Bet(p.money)
		if bet == "quit":
			break
		winnings = bet

		p.hand = []
		dealer.hand = []
		
		for i in range(2):
			p.hand.append(Deck.pop(0))
			dealer.hand.append(Deck.pop(0))
		
		dealer.hidden = dealer.hand.pop(0)


		print(f"Dealer's cards: {str(dealer.hand[0])} (hidden)")
		print()

		# hit/check loop
		while True:

			if (p.hand[0] == 'Ace' and p.hand[1] in Tens) or (p.hand[1] == 'Ace' and p.hand[0] in Tens):
				
				print("blackjack")
				winner = "p"
				winnings = math.floor(bet*1.5)

				break

			p.total = findTotal(p.hand)
			

			print(f"Your cards: {p.hand}")
			print(f"Total: {p.total}")
			
			if p.total > 21:
				winner = "dealer"
				print("you bust")
				time.sleep(bWT)
				break

			p.choice = input("(hit)/(check): ")

			if p.choice == "quit":
				menu = True
				break
			elif p.choice == "hit":
				hit(p.hand, Deck)
			elif p.choice == "check":
				break
			else:
				print("i dunno")

			print()
		
		if menu == True:
			break
		print()


		if winner == "p":
			print("player win")

			p.money += winnings
			dealer.money -= winnings

			input("Press enter to continue")
			print()

			continue
		
		elif winner == "dealer":
			print("dealer win")

			dealer.money += winnings
			p.money -= winnings
			
			if p.money < 1:
				print("sorry, outta cash")
				p.money += 200
			input("Press enter to continue")
			print()
			
			continue


		# dealer
		dealer.hand.append(dealer.hidden)

		dealer.total = findTotal(dealer.hand)

		print("The dealer flips his hidden card")
		printCards(dealer)
		time.sleep(dWT)
		print()

		while dealer.total < 17:

			hit(dealer.hand, Deck)
			dealer.total = findTotal(dealer.hand)
			printCards(dealer)
			if dealer.total > 21:
				print("dealer busts")
			time.sleep(bWT)
			print()
		
		if dealer.total > 21 or p.total > dealer.total:
			winner = "p"
		elif dealer.total > p.total:
			winner = "dealer"
		else:
			winner = "tie"
		

		if winner == "p":
			print("player win")

			p.money += winnings
			dealer.money -= winnings
		
		elif winner == "dealer":
			print("dealer win")

			dealer.money += winnings
			p.money -= winnings

		elif winner == "tie":
			print("tie")
		
		
		print(p.money)
		if p.money < 1:
			print("sorry, outta cash")
		input("Press enter to continue")
		print()
		
		
