import sys
import re
import dna.utils as utils


def rna_splice(dna, introns):
    """rna_splice(dna, introns) - given a dna string, it starts by removing the
    parameter introns from the dna string, and transcribing the resulting dna into
    rna"""
    # remove the introns from the dna
    dna = re.sub('|'.join(re.escape(intron) for intron in introns), '', dna)
    return utils.transcribe_protein(dna)


if __name__ == '__main__':
    dna = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
    introns = ['ATCGGTCGAA', 'ATCGGTCGAGCGTGT']
    if len(sys.argv) >= 2:
        fasta_set = utils.read_fasta(sys.argv[1])
        dna = fasta_set[0]
        introns = fasta_set[1:]
    print(rna_splice(dna, introns))
