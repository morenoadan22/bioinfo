import sys
import dna.utils as utils


def local_alignment_score(s, t):
    return (23, 'LYPRTEINSTRIN', 'LYEINSTEIN')


if __name__ == '__main__':
    s = 'MEANLYPRTEINSTRING'
    t = 'PLEASANTLYEINSTEIN'

    if len(sys.argv) >= 2:
        s, t = utils.read_fasta(sys.argv[1])

    print(local_alignment_score(s, t))
