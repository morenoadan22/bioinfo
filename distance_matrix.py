import sys
import dna.utils as utils
import point_mutations as pm


def p_distance(s1, s2):
    # hamming distance / total bases
    return pm.hamming_distance(s1, s2) / len(s1)


def distance_matrix(seq):
    rows = len(seq)
    columns = len(seq)
    matrix = [[0 for x in range(columns)] for x in range(rows)]
    for c in range(columns):
        for r in range(rows):
            matrix[r][c] = '{:.5f}'.format(p_distance(seq[r], seq[c]))
    return matrix


def pretty_print(matrix):
    for row in matrix:
        print(' '.join(row))


if __name__ == '__main__':
    seq = ['TTTCCATTTA', 'GATTCATTTC', 'TTTCCATTTT', 'GTTCCATTTA']
    if len(sys.argv) >= 2:
        seq = utils.read_fasta(sys.argv[1])
    pretty_print(distance_matrix(seq))
