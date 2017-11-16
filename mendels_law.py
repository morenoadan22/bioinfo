import sys
import dna.utils as utils


def calculate_mendels_probability(k, m, n):
    total = k + m + n
    # two reccessive genes
    rec_rec = (n / total) * ((n - 1) / (total - 1))
    # two hetero genes
    het_het = (m / total) * ((m - 1) / (total - 1))
    # a hetero and recessive
    het_rec = (m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))

    probability = rec_rec + het_het / 4 + het_rec / 2

    return 1 - probability


if __name__ == '__main__':
    dominant, heterozygous, homozygous = [2, 2, 2]
    if len(sys.argv) >= 2:
        dominant, heterozygous, homozygous = map(int, utils.read_file(sys.argv[1]).split(' '))
    print(calculate_mendels_probability(dominant, heterozygous, homozygous))
