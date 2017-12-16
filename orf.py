import sys
import dna.utils as utils
import rna_to_protein as trp
import reverse_complement as rvc


def search_frames(dna):
    frames = []
    indicies = []

    for i in range(len(dna)):
        protein = trp.translate_codon(dna[i:i + 3])
        if protein and protein == 'M':
            indicies.append(i)

    for i in indicies:
        stop = False
        frame = ''

        for j in range(i, len(dna), 3):
            protein = trp.translate_codon(dna[j:j + 3])

            if not protein:
                break

            if protein == 'Stop':
                stop = True
                break

            frame += protein

        if stop:
            frames.append(frame)

    return frames


if __name__ == '__main__':
    dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

    if len(sys.argv) >= 2:
        dna = utils.read_fasta(sys.argv[1])[0].strip()

    frames = set(search_frames(dna) + search_frames(rvc.complementary_nucleotide(dna)))
    print('\n'.join(frames))
