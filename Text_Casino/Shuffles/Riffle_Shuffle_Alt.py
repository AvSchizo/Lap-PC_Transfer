import copy

def lastIndex(list):
	return (len(list)-1)


def Riffle_Shuffle_Alt(deck):


	bottom = copy.deepcopy(deck)
	top = []

	i = 0
	while (len(deck)) > i*2:
		top.append(bottom.pop(0))
		i += 1
	
	returnDeck = []
	while True:
		if len(top) > 0:
			returnDeck.append(top.pop(-1))
		if len(bottom) > 0:
			returnDeck.append(bottom.pop(-1))
		if len(top) == 0 and len(bottom) == 0:
			break

	
	dos = deck
	for i in range(len(dos)):
		dos[i] = returnDeck[i]