import random
import math
import time

# from Save_Data import saveData, loadData


# True: "1" = first item in action list; False: disabled
numberedActions = True


startChoiceKey = "start"
quitChoiceKey = "quit"
konamiChoiceKey = "uuddlrlrba"

dDChoiceKey = "double down"
hitChoiceKey = "hit"
standChoiceKey = "stand"
splitChoiceKey = "split"


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


def findIndex(item, list):
	for i in range(len(list)):
		if list[i] == item:
			return i



class charClass():
	def __init__(self, money):
		self.money = money

class handClass():
	def __init__(self, taking, list):
		self.id = len(list)

		if self.id > 0:
			self.cards = [list[taking].cards.pop(0)]
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
		validActions = [startChoiceKey, quitChoiceKey]

		print()
		print("BLACKJACK")
		print()

		print(f"Actions: {validActions}")
		menuChoice = input("Choice: ")

		if menuChoice == startChoiceKey:
			print()
			break
		elif menuChoice == quitChoiceKey:
			quit()
		elif menuChoice == konamiChoiceKey:
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

		if len(Shoe) < 20:
			Shoe = newShoe(decksInShoe)
			print(f"New {decksInShoe} deck shoe")
			print()
		Deck = Shoe

		bet = Bet(p.money)
		if bet == "quit":
			break

		# list containing first empty hand
		handContainer = [handClass(0, [])]
		p.pile = handContainer[0]

		dealer.hand = []


		validActions = [hitChoiceKey, standChoiceKey, dDChoiceKey]
		
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

			p.pile.blCheck = 0
			p.pile.noEvenMoney = False
			p.pile.doubleDown = False
			p.pile.notPastCard = True
			p.pile.winnings = bet

			# hit/stand loop
			while True:

				if len(handContainer) > 1:
					print(f"Pile {handIteration + 1}")

				# reset split in actions
				if splitChoiceKey in validActions:
					validActions.pop(findIndex(splitChoiceKey, validActions))

				if len(p.hand) == 2:
					if p.hand[0] == p.hand[1] and p.money >= 2*bet:
						validActions.append(splitChoiceKey)
				

				# reset double down in actions
				if dDChoiceKey in validActions:
					validActions.pop(findIndex(dDChoiceKey, validActions))
				
				if p.money >= 2*bet and p.pile.notPastCard:
					validActions.append((dDChoiceKey))
				p.pile.notPastCard = False


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
							p.pile.notPastCard = True
							
							if evenMoney == "y":
								p.pile.winnings = bet
								p.pile.winner = "p"
								p.pile.noEvenMoney = True
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

				if p.pile.doubleDown:
					next()
					break


				if insurance[1] == 0 and dealer.hand[0] == 'Ace':

					while True:
							
						insurance[2] = input("Would you like insurance? (y)/(n): ")
						p.pile.notPastCard = True

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
					# quit
					if p.choice == quitChoiceKey:
						menu = True
						break
					# hit
					elif p.choice == hitChoiceKey:
						hit(p.hand, Deck)
					# double down
					elif p.choice == dDChoiceKey:
						if (p.money - p.pile.winnings) >= p.pile.winnings:
							p.pile.doubleDown = True
							p.pile.winnings *= 2
							print(p.pile.winnings)
							hit(p.hand, Deck)
						else:
							print("not enough money")
					# stand
					elif p.choice == standChoiceKey:
						break
					# split
					elif p.choice == splitChoiceKey:
						appendingId = handContainer[handIteration].id
						handContainer.append(handClass(appendingId, handContainer))
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
		

		for i in range(len(handContainer)):

			# blackjack and no dealer ace
			if handContainer[i].winner == "p":

				p.money += handContainer[i].winnings
				dealer.money -= handContainer[i].winnings

			
			# bust
			elif handContainer[i].winner == "dealer":

				# if bust, still lose insurance -> insurance[0] here
				dealer.money += handContainer[i].winnings + insurance[0]
				p.money -= handContainer[i].winnings + insurance[0]
				
				if p.money < 1:
					print("sorry, outta cash")
					p.money += debtMoney
		
		if not stillToPlay:			
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

			if handContainer[i].total > 21:
				continue
			if handContainer[i].blCheck > 0 and not handContainer[i].noEvenMoney:
				continue


			if len(handContainer) > 1:
				print(f"For pile {i + 1}:")

			if handContainer[i].winner == "p":

				if len(handContainer) > 1:
					print("player win")
				elif dealer.total < 22:
					print("player win")

				p.money += handContainer[i].winnings
				dealer.money -= handContainer[i].winnings

			
			elif handContainer[i].winner == "dealer":

				if len(handContainer) > 1:
					print("dealer win")
				elif handContainer[i].total < 22:
					print("dealer win")

				dealer.money += handContainer[i].winnings
				p.money -= handContainer[i].winnings

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
