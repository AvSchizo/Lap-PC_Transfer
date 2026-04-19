import copy


def cutDeck(deck):

	bottom = copy.deepcopy(deck)
	top = []

	i = 0
	while (len(deck)) > i*2:
		top.append(bottom.pop(0))
		i += 1
	
	returnDeck = bottom

	for i in range(len(top)):
		returnDeck.append(top.pop(0))
	print(returnDeck)
	

	dos = deck
	for i in range(len(dos)):
		dos[i] = returnDeck[i]


# Deck = []
# for i in range(10):
# 	Deck.append(i+1)

# cutDeck(Deck)
# print(Deck)
