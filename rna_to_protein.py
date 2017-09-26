import sys

data = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

def rnaToProtein(rna):
	protein = ""
	rna_codon_table = load_rna_codon_table('rna_codon.txt')		
	for i in range(0, len(data), 3):
		code = rna_codon_table[data[i:i+3]]
		if code == '*':
			break
		protein += rna_codon_table[data[i:i+3]]
	return protein


def readFile(filename):
	with open(filename, 'r') as file:
		contents = file.read().replace('\n', '')
	return contents

def load_rna_codon_table(filename):
	table = {}
	with open(filename, 'r') as file:
		content = file.readlines()

	for line in content:
		lineArray = line.split('      ')		
		for pair in lineArray:
			table[pair.split(' ')[0]] = pair.split(' ')[1].strip()
	return table

if __name__ == '__main__':	
	if len(sys.argv) >= 2:
		data = readFile(sys.argv[1])

	# print(load_rna_codon_table('rna_codon.txt'))
	answer = open('output/answer_7.txt', 'w')
	print >> answer, rnaToProtein(data)
	answer.close()
