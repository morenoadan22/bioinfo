import sys

data = "Bravely bold Sir Robin rode forth from Camelot\nYes, brave Sir Robin turned about\nHe was not afraid to die, O brave Sir Robin\nAnd gallantly he chickened out\nHe was not at all afraid to be killed in nasty ways\nBravely talking to his feet\nBrave, brave, brave, brave Sir Robin\nHe beat a very brave retreat"

def sliceEvenLines(dataList):
	newList = ""
	for num, l in enumerate(dataList):
		if (num + 1) % 2 == 0:
			newList += l
	return newList

def readFileIntoList(filename):
	with open(filename, 'r') as file:
		dataList = file.readlines()
	return dataList

if __name__ == '__main__':
	dataList = []
	if len(sys.argv) >= 2:
		dataList = readFileIntoList(sys.argv[1])
	else:
		dataList = data.split('\n')
	
	outputFile = open('output/answer_4.txt', 'w')	
	outputFile.write(str(sliceEvenLines(dataList)))
	outputFile.close()
