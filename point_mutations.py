import sys
import dna.utils as utils


def hamming_distance(s1, s2):
    hd = 0
    for i, j in zip(s1, s2):
        if i != j:
            hd += 1
    return hd


if __name__ == '__main__':
    s1 = 'GAGCCTACTAACGGGAT'
    s2 = 'CATCGTAATGACGGCCT'
    if len(sys.argv) >= 2:
        s1, s2 = utils.read_file_lines(sys.argv[1])

    print(hamming_distance(s1, s2))
