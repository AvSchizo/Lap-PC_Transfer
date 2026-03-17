import random

Suits = ('S', 'D', 'C', 'H')
Ranks = ('filler', 'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')
Poker_Hands = ('High Card', 'Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush', 'Five of a Kind')


def Create_Deck():

	deck = []

	for i in Suits:
		
		for v in range (1, 14):

			deck.append(str(i) + str(v))
	
	return(deck)

def Shuffle(deck):
	random.shuffle(deck)


def recycleDeck():

	tempDeck = Create_Deck()
	Shuffle(tempDeck)

	return tempDeck

Deck = recycleDeck()

def newHand():

	tempHand = []
	for i in range(5):
		tempHand.append(Deck.pop(0))

	return tempHand

def newHandAlt(deck):
	tempHand = []
	for i in range(5):
		tempHand.append(deck.pop(0))
	return tempHand

Hand = newHand()


def findAmount(item, list):

	iterations = 0

	for i in range(len(list)):

		if list[i] == item:

			iterations += 1
	
	return iterations

def findValues(hand):

	values = []

	for i in range(len(hand)):

		valueList = list(str(hand[i]))

		if valueList[0] in Suits:
			valueList.pop(0)

		values.append(int(''.join(valueList)))
	
	return values


# ofakind()
def ofakind(hand):
	
	values = findValues(hand)

	highest = 0
	rank = 0

	for i in range(len(values)):

		if values[i] == rank:
			continue

		tempAmount = findAmount(values[i], values)

		if tempAmount == 3 and highest == 2:
			return 'fullhouse', values[i], rank
		elif tempAmount == 2 and highest == 3:
			return 'fullhouse', rank, values[i]
		
		if tempAmount == highest and tempAmount == 2:
			return '2pair', values[i], rank
		
		elif tempAmount > highest:

			highest = tempAmount
			rank = values[i]
		
	return highest, rank

def ofaSuit(cards):

	highest = 0

	for i in range(len(Suits)):

		iterations = findAmount(Suits[i], cards)
		if iterations > highest:
			highest == iterations
	
	return highest



# flush()
def flush(hand):

	values = findValues(hand)
	values.sort(reverse=True)

	Suit = list(hand[0])[0]

	i = 0
	while i < 5:
		
		if list(hand[i])[0] != Suit:
			return False
		
		i += 1
	
	return True, values[0], values[1], values[2]

# straight()
def straight(hand):

	values = findValues(hand)

	values.sort()

	if values[0] == 1:

		if values[1] == 2 or values[1] == 10:

			if values[4] == values[1] + 3:
				return True, values[4]
			else:
				return False
		
		else:
			return False
	
	else:

		if values[4] == values[0] + 4:
			return True, values[4]
		else:
			return False




def getHandInfo(hand):

	if ofakind(hand)[0] == 'fullhouse' or ofakind(hand)[0] == '2pair':

		fullpair = ofakind(hand)
		
		if fullpair[0] == 'fullhouse':
			return 6, fullpair[1], fullpair[2]
		else:
			return 2, fullpair[1], fullpair[2]

	oak = ofakind(hand)[0]
	if oak > 1:

		oan = ofakind(hand)[1]

		if oak == 2:
			return 1, oan
		elif oak == 3:
			return 3, oan
		elif oak == 4:
			return 7, oan
		elif oak == 5:
			return 10, oan
	

	if flush(hand) == False:

		if straight(hand) == False:
			values = findValues(hand)
			values.sort(reverse=True)
			return 0, values[0]
		else:
			return 4, straight(hand)[1]
	
	else:

		if straight(hand) == False:
			return 5, flush(hand)[1], flush(hand)[2], flush(hand)[3]
		
		sh1 = straight(hand)[1]
		if sh1 == 13:
			return 9, sh1
		else:
			return 8, sh1


# printPokerHand()
def printPokerHand(hand):

	info = getHandInfo(hand)
	result = info[0]

	if result == 0:
		print("High Card of " + str(Ranks[info[1]]))

	elif result == 1:
		print("Pair of " + str(Ranks[info[1]]) + "s")
	
	elif result == 2 or result == 6:
		print(str(Poker_Hands[result]) + '; ' + str(Ranks[info[1]]) + "s and " + str(Ranks[info[2]]) + "s")
	
	elif result == 3:
		print("Three " + str(Ranks[info[1]]) + "s")
	elif result == 7:
		print("Four " + str(Ranks[info[1]]) + "s")
	elif result == 10:
		print("Five " + str(Ranks[info[1]]) + "s")

	else:
		print(Poker_Hands[result])


# comparePokerHand()
def comparePokerHand(hand1, hand2):

	frstInfo = getHandInfo(hand1)
	scndInfo = getHandInfo(hand2)

	if frstInfo[0] > scndInfo[0]:
		return 1
	elif frstInfo[0] < scndInfo[0]:
		return 2
	
	if frstInfo[1] > scndInfo[1]:
		return 1
	elif frstInfo[1] < scndInfo[1]:
		return 2
	
	result = frstInfo[0]
	if result == 5:

		if frstInfo[2] > scndInfo[2]:
			return 1
		elif frstInfo[2] < scndInfo[2]:
			return 2
		
		if frstInfo[3] > scndInfo[3]:
			return 1
		elif frstInfo[3] < scndInfo[3]:
			return 2
		
		return 0
	
	return 0
