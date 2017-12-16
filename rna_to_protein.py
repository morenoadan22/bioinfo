import sys

data = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
rna_codon_table = None


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
    'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def rna_to_protein(rna):
    protein = ''
    for i in range(0, len(data), 3):
        code = codon_table()[data[i:i + 3]]
        if code == '*':
            break
        protein += codon_table()[data[i:i + 3]]
    return protein


def translate_codon(codon):
    protein = None
    if len(codon) == 3 and codon in DNA_CODON_TABLE:
        protein = DNA_CODON_TABLE[codon]
    return protein


# def readFile(filename):
#     with open(filename, 'r') as file:
#         contents = file.read().replace('\n', '')
#     return contents


def codon_table():
    # if rna_codon_table is None:
    #     rna_codon_table = load_rna_codon_table('rna_codon.txt')
    return load_rna_codon_table('rna_codon.txt')


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
    print(rna_to_protein(data), file=answer)
    answer.close()
