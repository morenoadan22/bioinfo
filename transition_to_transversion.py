import sys

def parse_fasta(target):    
    data = []
    current_data = None
    for line in [l.strip() for l in target.splitlines()]:
        if line.startswith('>'):
        	if current_data != None:
        		data.append(current_data)
        	current_data = ''
        else:
            current_data += line            
    data.append(current_data)
    return data

def transitions():
	return [('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')]

def read_file(filename):
	data = ""
	with open(filename, 'r') as file:
		data = file.read()
	return data

def transition_transversion_ratio(s1, s2):
	ratio = {'transition': 0, 'transversion': 0}		
	for p in zip(s1, s2):
		if p[0] != p[1]:
			if p in transitions():
				ratio['transition'] += 1
			else:
				ratio['transversion'] += 1
	return ratio['transition'] / ratio['transversion']

if __name__ == '__main__':	
	s1 = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
	s2 = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"
	if len(sys.argv) >= 2:
		 data = read_file(sys.argv[1])		 		 
		 s1, s2 = parse_fasta(data)

	with open('output/answer_9.txt','w') as answer:	
		print(transition_transversion_ratio(s1, s2), end='', file=answer)	
		print('Output written to %s' % answer.name)




