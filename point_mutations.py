import sys
import dna.utils as utils


def hamming_distances(s1, s2):
    hd = 0
    for i, j in zip(s1, s2):
        if i != j:
            hd += 1
    return hd


def hamming_distance(seq1, seq2):
    mutations = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mutations += 1
    return mutations


if __name__ == '__main__':
    s1 = 'GAGCCTACTAACGGGAT'
    s2 = 'CATCGTAATGACGGCCT'
    if len(sys.argv) >= 2:
        s1, s2 = utils.read_file_lines(sys.argv[1])

    print(hamming_distance(s1, s2))
