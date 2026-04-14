import random
import math
import time

# from Save_Data import saveData, loadData


# True: "1" = first item in action list; False: disabled
numberedActions = True


# bust deal sleep time
bdST = .75

debtMoney = 200
minBet = 10

Ranks = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')
Tens = (10, 'Jack', 'Queen', 'King')

def checkNumberedActions(choice, actions):
	if numberedActions:
		if choice.isdigit():
			choice = int(choice)
			if choice > 0 and choice <= len(actions):
				return True

def next():
	input("Press ENTER to continue")

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
		print(f"Total: {char.total}")
	else:
		print(f"Player's cards: {char.pile.cards}")
		print(f"Total: {char.pile.total}")


def newShoe(decks):
	tempShoe = []

	for i in range(decks):

		for i in range(4):
			for i in range(13):
				tempShoe.append(Ranks[i])

	Shuffle(tempShoe)
	return tempShoe



class charClass():
	def __init__(self, money):
		self.money = money

class handClass():
	def __init__(self, list):
		self.id = len(list)

		if self.id > 0:
			self.cards = [list[self.id - 1].cards.pop(0)]
		else:
			self.cards = []
	
			
	total = 0
	winner = "none"
	blCheck = 0


decksInShoe = 5
Shoe = []
Deck = Shoe


p = charClass(200)
dealer = charClass(10000)



# making sure game loop goes into menu loop
while True:

	# menu loop
	while True:
		validActions = ["start", "quit"]

		print()
		print("BLACKJACK")
		print()

		print(f"Actions: {validActions}")
		menuChoice = input("Choice: ")

		if menuChoice == validActions[0]:
			print()
			break
		elif menuChoice == validActions[1]:
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
		stillToPlay = False

		# [0] = insurance amount; [1] = if asked for insurance; [2] = player answer
		insurance = [0, 0, ""]
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

		# list containing first empty hand
		handContainer = [handClass([])]
		p.pile = handContainer[0]

		dealer.hand = []


		validActions = ["hit", "stand", "double down"]
		
		for i in range(2):
			p.pile.cards.append(Deck.pop(0))
			dealer.hand.append(Deck.pop(0))
		
		dealer.hidden = dealer.hand.pop(0)


		# handContainer.append(handClass(handContainer))
		handIteration = 0
		# handContainer loop
		while True:
			p.pile = handContainer[handIteration]
			p.hand = handContainer[handIteration].cards
			p.total = handContainer[handIteration].total
			p.winner = handContainer[handIteration].winner

			p.pile.blCheck = 0

			if len(handContainer) > 1:
				print(f"Pile {handIteration + 1}")

			# hit/stand loop
			while True:
				
				print(f"Dealer's cards: {str(dealer.hand[0])} (hidden)")
				print()
				
				p.pile.total = findTotal(p.hand)
				printCards(p)

				if len(p.hand) > 1:
					if p.hand[0] == 'Ace' and p.hand[1] in Tens:
						p.pile.blCheck += 1
					if p.hand[1] == 'Ace' and p.hand[0] in Tens:
						p.pile.blCheck += 1

				if p.pile.blCheck > 0:
					
					if dealer.hand[0] == 'Ace':
						while True:
							evenMoney = input("even money? (y)/(n): ")
							
							if evenMoney == "y":
								p.pile.winnings = bet
								p.pile.winner == "p"
								break
							elif evenMoney == "n":
								break
							else:
								print("sorry, I don't understand")
					
					else:
						print()
						print("blackjack")
						next()
						p.pile.winner = "p"
						p.pile.winnings = math.floor(bet*1.5)

					break
				
				
				if p.pile.total > 21:
					time.sleep(bdST)
					p.pile.winner = "dealer"
					print()
					print("you bust")
					next()
					break

				if doubleDown:
					next()
					break


				if insurance[1] == 0 and dealer.hand[0] == 'Ace':

					while True:
							
						insurance[2] = input("Would you like insurance? (y)/(n): ")

						if insurance[2] == "y":
							insurance[0] = math.ceil(bet/2)
							break
						elif insurance[2] == "n":
							break
						else:
							print("I don't understand")
							print()
					
					insurance[1] = 1
					print()
					continue

				print()
				print(f"Actions: {validActions}")
				p.choice = input("Choice: ")

				if checkNumberedActions(p.choice, validActions):
					p.choice = validActions[int(p.choice) - 1]

				if p.choice in validActions:
					if p.choice == "quit":
						menu = True
						break
					# hit
					elif p.choice == validActions[0]:
						hit(p.hand, Deck)
					# double down
					elif p.choice == validActions[2]:
						if (p.money - winnings) >= winnings:
							doubleDown = True
							winnings *= 2
							hit(p.hand, Deck)
						else:
							print("not enough money")
					# stand
					elif p.choice == validActions[1]:
						break
					else:
						print("i dunno")
				else:
					print("not in actions")

				print()

			if handContainer[handIteration].id == handContainer[-1].id:
				break
			elif menu:
				break
			else:
				handIteration += 1
		
		if menu:
			break
		print()


		for i in range(len(handContainer)):

			if handContainer[i].winner == "p":
				pass
			elif handContainer[i].winner == "dealer":
				pass
			else:
				stillToPlay = True
		

		if not stillToPlay:
			for i in range(len(handContainer)):

				# blackjack
				if handContainer[i].winner == "p":

					p.money += winnings
					dealer.money -= winnings

				
				# bust
				elif handContainer[i].winner == "dealer":

					# if bust, still lose insurance -> insurance[0] here
					dealer.money += winnings + insurance[0]
					p.money -= winnings + insurance[0]
					
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
		

		for i in range(len(handContainer)):

			if dealer.total > 21 or handContainer[i].total > dealer.total:
				if handContainer[i].total < 22:
					handContainer[i].winner = "p"
				else:
					handContainer[i].winner = "dealer"
			elif dealer.total > handContainer[i].total:
				handContainer[i].winner = "dealer"
			else:
				handContainer[i].winner = "tie"
		

		# (dealer/p).total < 22 is so you don't have
		# "player busts" and "dealer wins" back to back

		for i in range(len(handContainer)):

			if len(handContainer) > 1:
				print(f"For pile {i + 1}:")

			if handContainer[i].winner == "p":

				if len(handContainer) > 1:
					print("player win")
				elif dealer.total < 22:
					print("player win")

				p.money += winnings
				dealer.money -= winnings

			
			elif handContainer[i].winner == "dealer":

				if len(handContainer) > 1:
					print("dealer win")
				elif handContainer[i].total < 22:
					print("dealer win")

				dealer.money += winnings
				p.money -= winnings

				if insurance[0] > 0 and dealer.hand[1] == 10:
					p.money += insurance[0]
					dealer.money -= insurance[0]


			elif handContainer[i].winner == "tie":

				if len(handContainer) > 1:
					print("dealer win")
				elif handContainer[i].total < 22 and dealer.total < 22:
					print("tie")

				if insurance[0] > 0 and dealer.hand[1] == 10:
					p.money += insurance[0]
					dealer.money -= insurance[0]
			
			if p.money < 1:
				print("sorry, outta cash")
				p.money += debtMoney
			

			if len(handContainer) > 1:
				next()
				print()
			elif handContainer[i].total < 22 and dealer.total < 22:
				next()
				print()
		
