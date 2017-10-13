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


def edit_distance(s, t):
    """edit_distance(s, t) - takes two sequences and returns the alignment score and the aligned strings"""
    m = setup_matrix(s, t)
    rows = len(s) + 1
    cols = len(t) + 1

    for c in range(1, cols):
        for r in range(1, rows):
            if s[r - 1] == t[c - 1]:
                match_cost = 0
            else:
                match_cost = 1
            # figure out which box to take the number from
            top = m[r - 1][c] + 1
            left = m[r][c - 1] + 1
            diagonal = m[r - 1][c - 1] + match_cost
            m[r][c] = min(top, left, diagonal)

    new_s, new_t = print_alignment(s, t, m)
    return m[r][c], new_s, new_t


def reverse_string(target):
    return target[::-1].upper()


def print_alignment(s, t, m):
    """print_alignment(s, t, m) - traces back through a matrix to figure out the two new strings with gaps"""
    gap = '-'
    new_s = ''
    new_t = ''

    i, j = len(s), len(t)

    while (not (i == 0 and j == 0)):
        current = m[i][j]

        neighbors = []

        if i != 0 and j != 0:
            neighbors.append(m[i - 1][j - 1])
        if i != 0:
            neighbors.append(m[i - 1][j])
        if j != 0:
            neighbors.append(m[i][j - 1])

        min_cost = min(neighbors)

        if current == min_cost:
            i, j = i - 1, j - 1
            new_s += s[i]
            new_t += t[j]
        elif (i != 0 and j != 0 and min_cost == m[i - 1][j - 1]):
            i, j = i - 1, j - 1
            new_s += s[i]
            new_t += t[j]
        elif (j != 0 and min_cost == m[i][j - 1]):
            i, j = i, j - 1
            new_s += gap
            new_t += t[j]
        elif (i != 0 and min_cost == m[i - 1][j]):
            i, j = i - 1, j
            new_s += s[i]
            new_t += gap

    return reverse_string(new_s), reverse_string(new_t)


if __name__ == '__main__':
    s = 'PRETTY'
    t = 'PRTTEIN'
    if len(sys.argv) >= 2:
        s, t = utils.read_fasta(sys.argv[1])
    for result in edit_distance(s, t):
        print(result)
