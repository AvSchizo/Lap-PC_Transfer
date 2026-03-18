import random

from Python_Poker_Hand import getHandInfo, printPokerHand, comparePokerHand
from Python_Poker_Hand import findValues, ofaSuit
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
		print("2) call [" + callCost + "]")
	print("3) raise")

	return int(input("Choice: "))

dealer = 'e'

eCur = 10
pCur = 10
def bet(round, pCur, eCur):

	pot = 0
	callCost = 0

	pCalled = 0
	eCalled = 0


	if dealer == 'e':

		print("Money: " + str(pCur))
		print("pot: " + str(pot))

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
		
	
	while True:

		print("pot: " + str(pot))
		print()

		# enemy turn
		if callCost == 0:

			if round == 1:

				curHandVal = findValues(eHand)
				curHandVal.sort()
				if curHandVal[0] > (curHandVal[4] - 6) or ofaSuit(eHand) >= 3:
					# enemy bets

					eCalled = 1
					pCalled = 0
					if eCur < 2:
						eRaise = 1
					else:
						eRaise = 2
					pot += eRaise + callCost
					eCur -= (eRaise + callCost)
					print("he raises by " + str(eRaise))
				
				else:
					# enemy checks
					eCalled = 1
					print("he checks")
			

			if round == 2:

				if random.randint(1, 20) == 1:
					# enemy checks
					eCalled = 1
					print("he checks")

				elif getHandInfo(eHand)[0] > 1:
					# enemy bets

					eCalled = 1
					pCalled = 0

					eRaise = random.randint(1, (eCur / 2))
					eCur -= eRaise

					pot += eRaise
					callCost = eRaise
				
				else:
					#enemy checks
					eCalled = 1
					print("he checks")

		
		else:
			# player bets

			if callCost > eCur:
				# enemy folds
				print("he folds")
				return 0
			
			else:
				# enemy calls

				eCalled = 1

				pot += callCost
				eCur -= callCost

				print("he calls")
		

		if pCalled == 1 and eCalled == 1:
			break

		print()

		# player turn
		print("Money: " + str(pCur))
		print("pot: " + str(pot))

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
bet(1, pCur, eCur)
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
bet(2, pCur, eCur)
print()

print("you have: " + printPokerHand(pHand))
print("he has: " + printPokerHand(eHand))
