import sys

data = "AGAATGACACCTGCCTTTGATTGGCTAAGAGCGCTCTCAGTTCACAAACTGTAGCACCACCCAAGGGGCCATTATACCGCCGTAATGTTACCGATTACCGCTACAGCGGTTAAGGCCTTTTGCCCGGGGCCCCAAGCACGATCCACAATGTAAGAACCGAACCTGCAAGTTCGTAACCCACACGACATTACTGATGTCGCTAGCGATCTCCGCGAAAAGCTACATGTTGCCGCCGGACCTTTATCTGCCTTGTCCAAACTTAGGCCGTTCGTCATCCCACAGTTATAGCTAAGTGCGTCGTCAAATACGGTATGGCCTCCACAGCTCCTTTTGATGAGCCACAGCAAAACCGTCGGGTGATGCAGGGTACCGGCCTGCTCGCGTTCGGCTGTGAGTCAATTCGCATGAGGTCATCGCCAACGCCATCAGACTTCGTGCCTTGAGTACTCCAGTGCTAGGAAGAGTTTGGGCAGACTCTATCGGGCGTTCTCATTGATTGCATCGTCAGGGTCTCTCTAAAACATGCGGCCGTTTGTATCAGCCTGCTGAACGCTTCGTGGTCCGCAGACTGAAGACCTCTTCAAATCAACCTCTTATATCACACCGGCACCATCGTCGGGCACGTTCACCGGGGCGGGGAGACCGATAAGCGCACGCATCGGTCCTCAAAAAGATCAATGCTACAGGTGGTGTGATGTAGTACCTTCATTGGTCCTCAATTTTCAAGATACCCATCGCACAATCCGCTGGAACATCTAACGGTGTATCAGGCCTCGGCTCCCCAGAAATGAGAACGTTTTGGCGGTCAGTATTAACTTCGTCGGAGAGCAGTCGAGACCCATGATATCTGTCGTATCCTGTGGCGACCTAAATCTCCTGCGGGACTATACATAGTTTAACCAGGATTATTTACCCTTTGGGGCCACGTGGGAAAGAGTGCCGACTC"

def readFile(filename):
	with open(filename, 'r') as file:
		contents = file.read().replace('\n', '')
	return contents

def transcribe(dna):
	return dna.replace('T', 'U')

if __name__ == '__main__':	
	if len(sys.argv) >= 2:
		data = readFile(sys.argv[1])
		
	print transcribe(data)
