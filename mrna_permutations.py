import sys

AMINO_ACID_TO_NUMBER_OF_CODONS_DICT = {
    'A':4,
    'C':2,
    'D':2,
    'E':2,
    'F':2,
    'G':4,
    'H':2,
    'I':3,
    'K':2,
    'L':6,
    'M':1,
    'N':2,
    'P':4,
    'Q':2,
    'R':6,
    'S':6,
    'T':4,
    'V':4,
    'W':1,
    'Y':2
}

def read_file(filename):
	data = ""
	with open(filename, 'r') as file:
		data = file.read()
	return data

def calculate_posible_outcomes(data):
	product = 1	
	for aa in data:
		product *= AMINO_ACID_TO_NUMBER_OF_CODONS_DICT[aa]
	product *= 3 #stop codon
	return product % 1000000


if __name__ == '__main__':	
	dna = "MA"
	if len(sys.argv) >= 2:
		 dna = read_file(sys.argv[1])		 		 		 

	with open('output/answer_10.txt','w') as answer:	
		print(calculate_posible_outcomes(dna), end='', file=answer)	
		print('Output written to %s' % answer.name)

		