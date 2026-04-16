import random
import copy


def BC_Shuffle(deck):
	pileSizeParam = [0, 0]
	pileSizeParam[0] = 1
	pileSizeParam[1] = 3

	ref = copy.deepcopy(deck)

	returnDeck = []

	fb = 1
	while len(ref) > 0:

		pile = []
		
		pileSize = random.randint(pileSizeParam[0], pileSizeParam[1])
		if pileSize > len(ref):
			pileSize = len(ref)
		

		if fb % 2 == 0:
			for i in range(pileSize):
				pile.insert(0, ref.pop(0))
			
			for i in range(len(pile)):
				returnDeck.insert(0, pile.pop(0))
		
		else:
			for i in range(pileSize):
				pile.append(ref.pop(0))
			
			for i in range(len(pile)):
				returnDeck.append(pile.pop(0))
		
		fb += 1

	
	dos = deck
	for i in range(len(dos)):
		dos[i] = returnDeck[i]


# Deck = []
# for i in range(20):
# 	Deck.append(i+1)

# for i in range(1):
# 	BC_Shuffle(Deck)
# print(Deck)