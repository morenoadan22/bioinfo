import sys


def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read().replace('\n', '')
    return contents


def reverse_string(target):
    return target[::-1].upper()


def complementary_nucleotide(dna):
    complementary_nucleotide = reverse_string(dna)
    complementary_nucleotide = complementary_nucleotide.replace('A', 't')
    complementary_nucleotide = complementary_nucleotide.replace('T', 'a')
    complementary_nucleotide = complementary_nucleotide.replace('C', 'g')
    complementary_nucleotide = complementary_nucleotide.replace('G', 'c')
    return complementary_nucleotide.upper()


if __name__ == '__main__':
    data = "AAAACCCGGT"
    if len(sys.argv) >= 2:
        data = read_file(sys.argv[1])

    with open('output/answer_8.txt', 'w') as answer:
        print(complementary_nucleotide(data), end='', file=answer)
