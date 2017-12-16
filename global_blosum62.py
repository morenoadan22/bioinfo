import sys
import dna.utils as utils
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist


def global_alignment(s, t):
    """global_alignment(s,t) performs a global alignment using the BLOSUM62 matrix
    takes in two protein strings s and t (each length at most 1000aa)
    """
    matrix = matlist.blosum62
    return pairwise2.align.globalds(s, t, matrix, -5, -5)


if __name__ == '__main__':
    file_content = '>Rosalind_67\nPLEASANTLY\n>Rosalind_17\nMEANLY'

    if len(sys.argv) >= 2:
        file_content = utils.read_file(sys.argv[1])

    s, t = utils.parse_fasta(file_content)
    print('{:.0f}'.format(global_alignment(s, t)[0][2]))
