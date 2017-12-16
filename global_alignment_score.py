import sys
import dna.utils as utils


def setup_matrix(s, t):
    rows = len(s) + 1
    columns = len(t) + 1
    matrix = [[0 for x in range(columns)] for x in range(rows)]
    for i in range(1, rows):
        matrix[i][0] = i
    for j in range(1, columns):
        matrix[0][j] = j
    return matrix


def global_alignment_score(s, t):
    m = setup_matrix(s, t)
    rows = len(s) + 1
    cols = len(t) + 1

    for c in range(1, cols):
        for r in range(1, rows):
            if s[r - 1] == t[c - 1]:
                match_cost = 0
            else:
                match_cost = 5
            # figure out which box to take the number from
            top = m[r - 1][c] + 1
            left = m[r][c - 1] + 1
            diagonal = m[r - 1][c - 1] + match_cost
            m[r][c] = min(top, left, diagonal)

    return m[r][c]


if __name__ == '__main__':
    s = 'IASNDCMH'
    t = 'DCMHNIAS'

    if len(sys.argv) >= 2:
        s, t = utils.read_fasta(sys.argv[1])

    score = global_alignment_score(s, t)
    print(score)
