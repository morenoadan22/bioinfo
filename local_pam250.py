import sys
import dna.utils as utils
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist


def local_alignment(s, t):
    """local_alignment(s, t) performs a local alignment using the PAM250 matrix,
    aligns protein strings s and t and returns a possible alignment array
    """
    matrix = matlist.pam250
    return pairwise2.align.localds(s, t, matrix, -5, -5)


if __name__ == '__main__':
    file_content = '>Rosalind_67\nMEANLYPRTEINSTRING\n>Rosalind_17\nPLEASANTLYEINSTEIN'

    if len(sys.argv) >= 2:
        file_content = utils.read_file(sys.argv[1])

    s, t = utils.parse_fasta(file_content)
    alignment = local_alignment(s, t)[0]
    score = int(alignment[2])
    span = (alignment[3], alignment[4])
    new_s = alignment[0][span[0]: span[1]]
    new_t = alignment[1][span[0]: span[1]]
    print('\n'.join([str(score), new_s.replace('-', ''), new_t.replace('-', '')]))
