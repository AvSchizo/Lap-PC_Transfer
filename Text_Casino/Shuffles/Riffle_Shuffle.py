import random
import copy

def lastIndex(list):
	return (len(list)-1)


def Riffle_Shuffle(deck):


	bottom = copy.deepcopy(deck)
	top = []

	i = 0
	while (len(deck)) > i*2:
		top.append(bottom.pop(0))
		i += 1

	
	returnDeck = []

	returnDeck.append(top.pop(-1))
	while len(top) > 1 and len(bottom) > 1:
		if random.randint(0, 1) == 1:
			returnDeck.append(top.pop(-1))
		else:
			returnDeck.append(bottom.pop(-1))


	if len(top) == 1 and len(bottom) == 1:
		returnDeck.append(top.pop(-1))
		returnDeck.append(bottom.pop(-1))
	
	elif len(top) == 1:
		returnDeck.append(top.pop(-1))
		for i in range(len(bottom)):
			returnDeck.append(bottom.pop(-1))
	
	elif len(bottom) == 1:
		for i in range(len(top)):
			returnDeck.append(top.pop(-1))
		returnDeck.append(bottom.pop(-1))

	

	dos = deck
	for i in range(len(dos)):
		dos[i] = returnDeck[i]