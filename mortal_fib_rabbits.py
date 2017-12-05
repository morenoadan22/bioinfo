import sys
import dna.utils as utils


def remaining_rabbits(n, m):
    sequence = [1, 1]

    for i in range(n - 2):
        tmp = 0
        if i + 2 < m:
            tmp = sequence[i] + sequence[i + 1]
        else:
            tmp = sum(sequence[i - (m - 2): i + 1])
        sequence.append(tmp)

    return sequence[-1]


if __name__ == '__main__':
    n = 6
    m = 3
    if len(sys.argv) >= 2:
        n, m = utils.read_file_lines(sys.argv[1])[0].split()
        n = int(n)
        m = int(m)
    print(remaining_rabbits(n, m))
