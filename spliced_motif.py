import sys
import dna.utils as utils


def find_motif_indices(s, t):
    indices = []
    index = 0
    new_s = s[index:]
    for c in t:
        new_s = s[index:]
        index = new_s.index(c) + 1 + index
        indices.append(index)
    return indices


if __name__ == '__main__':
    s = 'ACGTACGTGACG'
    t = 'GTA'
    if len(sys.argv) >= 2:
        s, t = utils.read_fasta(sys.argv[1])
    print(' '.join(map(str, find_motif_indices(s, t))))
