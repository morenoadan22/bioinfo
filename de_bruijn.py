import sys
import dna.utils as utils
import reverse_complement as rvc


def edge(elmmt, k):
    return '(' + elmmt[0:k - 1] + ',' + elmmt[1:k] + ')'


def de_bruijn(sequences):
    edge_nodes = set()
    for s in sequences:
        edge_nodes.add(s)
        edge_nodes.add(rvc.complementary_nucleotide(s))

    k = len(sequences[0])
    edge_nodes = [edge(element, k) for element in edge_nodes]

    return edge_nodes


if __name__ == '__main__':
    sequences = ['TGAT', 'CATG', 'TCAT', 'ATGC', 'CATC', 'CATC']
    if len(sys.argv) >= 2:
        data = utils.read_file(sys.argv[1])
        sequences = data.splitlines()

    graph = de_bruijn(sequences)

    with open('output/answer_13.txt', 'w') as answer:
        print('\n'.join(graph), file=answer)
