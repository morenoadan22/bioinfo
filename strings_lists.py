import sys

data = "EGWq165H9h5F6JUnciaQe6fFRkphtk6T3WbItkW2jkIaf7cYqKm8auXgiKEMpJTD1yBZSnSdPmZ7WvTVe8rpunctatuseESPiy8xwq5uzt3aoy3Ix9TAcGaJjpqchU9d8ca6vI8ZqP7Amu0JSZZQ4HK1OVu6up3imQF3th3TfU3."

firstIndex = 14
secondIndex = 18
thirdIndex = 83
fourthIndex = 91


def readFile(filename):
    with open(filename, 'r') as file:
        contents = file.read().replace('\n', '')
    return contents


def sliceInclusively(string, a, b, c, d):
    return string[a:b + 1] + ' ' + string[c:d + 1]


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        data = readFile(sys.argv[1])
        firstIndex = sys.argv[2]
        secondIndex = sys.argv[3]
        thirdIndex = sys.argv[4]
        fourthIndex = sys.argv[5]

    f = open('string_lists_output.txt', 'w')
    print >> f, sliceInclusively(data, firstIndex, secondIndex, thirdIndex, fourthIndex)
    f.close()
