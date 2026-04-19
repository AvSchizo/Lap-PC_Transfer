
import json

def loadData(fileName):
	with open(fileName, "r") as f:
		return json.load(f)

def saveData(fileName, key, value):
	data = loadData(fileName)
	data[key] = value
	with open(fileName, "w") as f:
		json.dump(data, f)
	
