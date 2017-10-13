import sys
import dna.utils as utils
import kmers as km


def shared_motif(seq):
    k = min(map(len, seq))
    while not find_highest_k(seq, k):
        k -= 1
    for kmer in km.kmer(k, seq[0]).values():
        if found_in_sequence(seq[1:], kmer):
            return kmer


def found_in_sequence(seq, kmer):
    for s in seq:
        if kmer not in s:
            return False
    return True


def find_highest_k(seq, k):
    s1 = seq[0]
    kmers = km.kmer(k, s1).values()
    for s in seq[1:-1]:
        if any(kmer in s for kmer in kmers):
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    sequences = ['GATTACA', 'TAGACCA', 'ATACA']
    if len(sys.argv) >= 2:
        sequences = utils.read_fasta(sys.argv[1])

    print(shared_motif(sequences))
