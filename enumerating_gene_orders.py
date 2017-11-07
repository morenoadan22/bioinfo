import sys
import itertools as it


def enumerate_genes(num):
    return it.permutations(range(1, num + 1))


if __name__ == '__main__':
    dataset = 5
    if len(sys.argv) >= 2:
        dataset = sys.argv[1]

    gene_orders = list(enumerate_genes(dataset))

    print(len(gene_orders))
    for p in gene_orders:
        print(*p, sep=' ')
