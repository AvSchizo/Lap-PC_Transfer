import random


def Random_Shuffle(deck):

	for i in range(1000):
		deck.insert(0, deck.pop(random.randint(0, (len(deck)-1))))



Deck = []
for i in range(20):
	Deck.append(i+1)

for i in range(5):
	Random_Shuffle(Deck)
print(Deck)