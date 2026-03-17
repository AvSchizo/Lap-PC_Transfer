import random

from Python_Poker_Hand import getHandInfo, printPokerHand, comparePokerHand
from Python_Poker_Hand import recycleDeck, newHand, newHandAlt

print()
print("'S' = Spades")
print("'H' = Hearts")
print("'D' = Diamonds")
print("'C' = Clubs")
print()

Deck = recycleDeck()

pHand = newHand()
eHand = newHand()

def pBetChoice(callCost):

	print("1) fold")
	if callCost == 0:
		print("2) check")
	else:
		print("2) call")
	print("3) raise")

	return int(input("Choice: "))

dealer = 'e'

eCur = 10
pCur = 10
def bet(pCur, eCur):

	pot = 0
	callCost = 0

	pCalled = 0
	eCalled = 0


	if dealer == 'e':

		print("Money: " + str(pCur))
		print("pot:")
		print(pot)

		pChoice = pBetChoice(callCost)

		if pChoice == 1:
			return 0
		
		elif pChoice == 2:
			if callCost > 0:
				pot += pCur - callCost
				pCur -= callCost
			pCalled = 1
		
		elif pChoice == 3:
			while True:
				pRaise = int(input("Raise amount: "))
				if pRaise + callCost <= pCur:
					break
			pot += pRaise + callCost
			pCur -= (pRaise + callCost)
			callCost = pRaise
			pCalled = 1
		
		print()
	
	while True:

		print("pot:")
		print(pot)

		# enemy turn
		if callCost == 0:

			if getHandInfo(eHand)[0] > 0:

				eCalled = 1
				pCalled = 0
				if eCur < 2:
					eRaise = 1
				else:
					eRaise = 2
				pot += eRaise + callCost
				eCur -= (pRaise + callCost)
			
			else:
				eCalled = 1
				print("he checks")
		
		else:

			if callCost > eCur:
				print("he folds")
				return 0
			
			else:

				eCalled = 1

				pot += callCost
				eCur -= callCost

				print("he calls")
		

		if pCalled == 1 and eCalled == 1:
			break

		print()

		# player turn
		print("Money: " + str(pCur))
		print("pot:")
		print(pot)

		pChoice = pBetChoice(callCost)

		if pChoice == 1:
			return 0
		
		elif pChoice == 2:
			if callCost > 0:
				pot += (pCur - callCost)
				pCur -= callCost
			pCalled = 1
		
		elif pChoice == 3:
			while True:
				pRaise = int(input("Raise amount: "))
				if pRaise + callCost <= pCur:
					break
			
			pot += pRaise + callCost
			pCur -= (pRaise + callCost)
			callCost = pRaise
			pCalled = 1
			eCalled = 0
		
		if pCalled == 1 and eCalled == 1:
			break

		print()



print(pHand)
bet(pCur, eCur)
print()

#player card swap
pDiscard = input("cards to discard: ").split()
for i in range(len(pDiscard)):
	pDiscard[i] = int(pDiscard[i]) -1

for i in range(len(pDiscard)):

	pHand.pop(int(pDiscard[i]) - i)

for i in range(5 - len(pHand)):
	pHand.append(Deck.pop(0))

print()

print(pHand)
bet(pCur, eCur)
print()

printPokerHand(pHand)
printPokerHand(eHand)
