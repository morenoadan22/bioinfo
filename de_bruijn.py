import sys
import dna.utils as utils
from dna.node import Node
from dna.de_bruijn_graph import DeBruijnGraph
from kmers import kmer


def draw_graph(sequences):
    graph = DeBruijnGraph()
    for read in sequences:
        # split into kmers
        for k in kmer(3, read).values():
            # create nodes with edges
            graph.append(Node(k))
    return graph


if __name__ == '__main__':
    sequences = ['GGAAATTT', 'AGGAAACG', 'CGGGGAAA', 'CGAAAA']
    if len(sys.argv) >= 2:
        data = utils.read_file(sys.argv[1])
        sequences = utils.read_fasta(data)

    print(draw_graph(sequences))
