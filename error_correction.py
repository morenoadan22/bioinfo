import sys
import reverse_complement as rvc
import dna.utils as utils
import point_mutations as pm


def split_reads(seq, new_seq):
    valid = []
    invalid = []
    # loop through the reverse complement list
    for s in new_seq:
        # for each one, check if the current
        if new_seq.count(s) >= 2:
            valid.append(s)
        elif s in seq:
            invalid.append(s)
    return set(valid), set(invalid)


def generate_reverse_complements(seq):
    new_set = []
    for s in seq:
        new_set.append(s)
        new_set.append(rvc.complementary_nucleotide(s))
    return new_set


def determine_corrections(valid, invalid):
    corrections = []
    for iv in invalid:
        for v in valid:
            if pm.hamming_distance(iv, v) == 1:
                corrections.append([iv, v])
    return corrections


if __name__ == '__main__':
    fasta_file = 'datasets/error_reads_test.fasta'
    if len(sys.argv) >= 2:
        fasta_file = sys.argv[1]

    data = utils.read_fasta(fasta_file)
    new_data = generate_reverse_complements(data)
    valid, invalid = split_reads(data, new_data)
    for i in determine_corrections(valid, invalid):
        print("->".join(i))
