import sys

data = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
rna_codon_table = None


def rnaToProtein(rna):
    protein = ''
    for i in range(0, len(data), 3):
        code = codon_table()[data[i:i + 3]]
        if code == '*':
            break
        protein += codon_table()[data[i:i + 3]]
    return protein


def translate_codon(codon):
    protein = None
    if len(codon) == 3 and codon_table() in (codon):
        protein = rna_codon_table[codon]
    return protein


def readFile(filename):
    with open(filename, 'r') as file:
        contents = file.read().replace('\n', '')
    return contents


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
    print(rnaToProtein(data), file=answer)
    answer.close()
