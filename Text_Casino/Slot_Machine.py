import random
import math
import time


def turn(column):
	column.append(column.pop(0))

def turnAll(cC, c):

	for i in range(3):
		turn(cC[c[i]])


def showMachine(cC, ref):
	for i in range(3):
		print(f"	[{cC[ref[0]][i-1]}] [{cC[ref[1]][i-1]}] [{cC[ref[2]][i-1]}]")


c = ["column1", "column2", "column3"]

cC = {}
for i in range(3):
	cC[c[i]] = []
	for e in range(9):
		cC[c[i]].append(e+1)




for i in range(random.randint(9, 15)):

	turnAll(cC, c)
	
	showMachine(cC, c)
	print()
	time.sleep(.1)

for i in range(random.randint(9, 15)):

	turn(cC["column2"])
	turn(cC["column3"])
	
	showMachine(cC, c)
	print()
	time.sleep(.1)

for i in range(random.randint(9, 15)):

	turn(cC["column3"])
	
	showMachine(cC, c)
	print()
	time.sleep(.1)