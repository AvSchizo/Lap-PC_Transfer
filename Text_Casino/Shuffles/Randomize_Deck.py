import random
import copy


def Randomize(deck):

	ref = copy.deepcopy(deck)
	crop = []

	for i in range(len(deck)):
		crop.append(ref.pop(random.randint(0, len(ref)-1)))
	
	dos = deck
	for i in range(len(dos)):
		dos[i] = crop[i]


# Deck = []
# for i in range(20):
# 	Deck.append(i+1)

# for i in range(1):
# 	Randomize(Deck)
# print(Deck)