import random
import math
import time

# from Save_Data import saveData, loadData


# True: "1" = first item in action list; False: disabled
numberedActions = True


# bust deal sleep time
bdST = .75

debtMoney = 200

Ranks = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')
Tens = (10, 'Jack', 'Queen', 'King')

def checkNumberedActions(choice, actions):
	if numberedActions:
		if choice.isdigit():
			choice = int(choice)
			if choice > 0 and choice <= len(actions):
				return True

def next():
	input("Press enter to continue")

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
	hand.append(deck.pop(0))


def printCards(char):
	if char == dealer:
		print(f"Dealer's cards: {char.hand}")
	else:
		print(f"Player's cards: {char.hand}")
	print(f"Total: {char.total}")


def newShoe(decks):
	tempShoe = []

	for i in range(decks):

		for i in range(4):
			for i in range(13):
				tempShoe.append(Ranks[i])

	Shuffle(tempShoe)
	return tempShoe



class playerChar():
	def __init__(self, money):
		self.money = money


decksInShoe = 1
Shoe = []
Deck = Shoe


p = playerChar(200)
dealer = playerChar(10000)


# making sure game loop goes into menu loop
while True:

	# menu loop
	while True:
		print()
		print("MAIN MENU")
		print()

		print('"start"')
		print('"quit"')
		menuChoice = input("Choice: ")

		if menuChoice == "start":
			print()
			break
		elif menuChoice == "quit":
			quit()
		elif menuChoice == "uuddlrlrba":
			if p.money < 1000:
				p.money = 1000
			print()
			break
		else:
			print("Sorry, I don't understand")

	# round loop
	while True:

		menu = False
		winner = "none"
		blCheck = 0

		doubleDown = False

		if len(Shoe) < 20:
			Shoe = newShoe(decksInShoe)
			print(f"New {decksInShoe} deck shoe")
			print()
		Deck = Shoe

		bet = Bet(p.money)
		if bet == "quit":
			break
		winnings = bet

		p.hand = []
		dealer.hand = []

		validActions = ["hit", "check", "double down"]
		
		for i in range(2):
			p.hand.append(Deck.pop(0))
			dealer.hand.append(Deck.pop(0))
		
		dealer.hidden = dealer.hand.pop(0)


		# hit/check loop
		while True:
			
			print(f"Dealer's cards: {str(dealer.hand[0])} (hidden)")
			print()
			
			p.total = findTotal(p.hand)
			printCards(p)

			if p.hand[0] == 'Ace' and p.hand[1] in Tens:
				blCheck += 1
			if p.hand[1] == 'Ace' and p.hand[0] in Tens:
				blCheck += 1

			if blCheck > 0:
				
				if dealer.hand[0] == 'Ace':
					while True:
						evenMoney = input("even money? (y)/(n): ")
						
						if evenMoney == "y":
							winnings = bet
							winner = "p"
							break
						elif evenMoney == "n":
							break
						else:
							print("sorry, I don't understand")
				
				else:
					print()
					print("blackjack")
					next()
					winner = "p"
					winnings = math.floor(bet*1.5)

				break
			
			
			if p.total > 21:
				time.sleep(bdST)
				winner = "dealer"
				print()
				print("you bust")
				next()
				break

			if doubleDown:
				next()
				break


			print()
			print(f"Actions: {validActions}")
			p.choice = input("Choice: ")

			if checkNumberedActions(p.choice, validActions):
				p.choice = validActions[int(p.choice) - 1]

			if p.choice in validActions:
				if p.choice == "quit":
					menu = True
					break
				elif p.choice == "hit":
					hit(p.hand, Deck)
				elif p.choice == "double down":
					if (p.money - winnings) >= winnings:
						doubleDown = True
						winnings *= 2
						hit(p.hand, Deck)
					else:
						print("not enough money")
				elif p.choice == "check":
					break
				else:
					print("i dunno")
			else:
				print("not in actions")

			print()
		
		if menu:
			break
		print()


		# player gets blackjack or busts

		if winner == "p":

			p.money += winnings
			dealer.money -= winnings

			next()
			print()

			continue
		
		elif winner == "dealer":

			dealer.money += winnings
			p.money -= winnings
			
			if p.money < 1:
				print("sorry, outta cash")
				p.money += debtMoney
			
			continue


		# dealer
		dealer.hand.append(dealer.hidden)

		dealer.total = findTotal(dealer.hand)

		print("The dealer flips his hidden card")
		printCards(dealer)
		next()
		print()

		if not doubleDown:
			while dealer.total < 17:

				print(f"The dealer deals a {Deck[0]}")
				hit(dealer.hand, Deck)
				dealer.total = findTotal(dealer.hand)
				printCards(dealer)
				if dealer.total > 21:
					time.sleep(bdST)
					print()
					print("dealer busts")
				next()
				print()
		
		if dealer.total > 21 or p.total > dealer.total:
			winner = "p"
		elif dealer.total > p.total:
			winner = "dealer"
		else:
			winner = "tie"
		

		if winner == "p":
			if dealer.total < 22:
				print("player win")

			p.money += winnings
			dealer.money -= winnings
		
		elif winner == "dealer":
			if p.total < 22:
				print("dealer win")

			dealer.money += winnings
			p.money -= winnings

		elif winner == "tie":
			if p.total < 22 and dealer.total < 22:
				print("tie")
		
		if p.money < 1:
			print("sorry, outta cash")
			p.money += debtMoney
		
		if p.total < 22 and dealer.total < 22:
			next()
			print()
		
