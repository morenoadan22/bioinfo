import sys
import dna.utils as utils
import reverse_complement as rc
import rna_to_protein as trp


def search_frames(dna):
    initial = []


if __name__ == '__main__':
    fafsta = [
        'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG']

    if len(sys.argv) >= 2:
        fafsta = utils.read_fasta(sys.argv[1])

    for dna in fafsta:
