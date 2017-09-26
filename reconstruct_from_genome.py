import sys

def read_file_lines(filename):
	data = []
	with open(filename, 'r') as file:
		data = file.readlines()
	return data

def read_file(filename):
	data = ''
	with open(filename, 'r') as file:
		data = file.read()
	return data

def reconstruct(pattern):
	dna = ''
	for idx,p in enumerate(pattern):
		if idx < len(pattern) - 1:
			dna += p[0]		
		else:
			dna += p
	return dna


if __name__ == '__main__':	
	pattern = ['ACCGA','CCGAA','CGAAG','GAAGC','AAGCT']
	if len(sys.argv) >= 2:
		 pattern = read_file_lines(sys.argv[1])

	with open('output/answer_12.txt','w') as answer:	
		print(reconstruct(pattern), end='', file=answer)	
		print('Output written to %s' % answer.name)

	# expected = read_file('output/expected_12.txt')
	# output = read_file('output/answer_12.txt')
	# print("Lengths are equal:")
	# print(len(expected) == len(output))
	# print("Content is identical:")
	# print(expected.strip() == output.strip())	
	