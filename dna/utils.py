def read_fasta(filename):
    data = read_file(filename)
    return parse_fasta(data)


def parse_fasta(target):
    data = []
    current_data = None
    for line in [l.strip() for l in target.splitlines()]:
        if line.startswith('>'):
            if current_data is not None:
                data.append(current_data)
            current_data = ''
        else:
            current_data += line
    data.append(current_data)
    return data


def read_file(filename):
    data = ''
    with open(filename, 'r') as file:
        data = file.read()
    return data


def read_file_lines(filename):
    data = ''
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


DNA_CODON_TABLE = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': '-', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': '-', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': '-', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def transcribe_protein(dna):
    result = ''
    for i in range(0, len(dna), 3):
        codon = dna[i:i + 3]
        protein = None

        if codon in DNA_CODON_TABLE:
            protein = DNA_CODON_TABLE[codon]

        if protein == '-':
            break

        if protein:
            result += protein

    return ''.join(list(result))
