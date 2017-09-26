import sys

data = "We tried list and we tried dicts also we tried Zen"


def readFile(filename):
    with open(filename, 'r') as file:
        contents = file.read().replace('\n', '')
    return contents


def countWords(target):
    wordMap = {}
    for token in target.split(' '):
        wordMap[token] = wordMap.get(token, 0) + 1
    return wordMap


def prettyPrint(map):
    formatted = ""
    for k, v in map.items():
        formatted += '{:s} {:d}\n'.format(k, v)
    return formatted


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        data = readFile(sys.argv[1])

    wordMap = countWords(data)
    outputFile = open('output/answer_5.txt', 'w')
    print >> outputFile, prettyPrint(wordMap)
    outputFile.close()
