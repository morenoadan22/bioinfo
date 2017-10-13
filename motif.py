import sys
import dna.utils as utils


def find_motifs(s1, s2):
    motfis = []
    for i in range(len(s1) - len(s2)):
        if s2 == s1[i:i + len(s2)]:
            motfis.append(i + 1)
    return motfis


if __name__ == '__main__':
    s1 = 'GATATATGCATATACTT'
    s2 = 'ATAT'
    if len(sys.argv) >= 2:
        s1, s2 = utils.read_file_lines(sys.argv[1])

    print(' '.join(map(str, find_motifs(s1, s2))))
