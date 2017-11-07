import itertools as it
import sys
import dna.utils as utils


def enumerate_oriented_gene_orders(n):
    """enumerate_oriented_gene_orders(n) -
        given an integer 'n', calculates all the possible permutations from
        1 to 'n' without repeating signs"""
    permutations = list(it.permutations(range(1, n + 1)))
    prefixes = list(it.product('-+', repeat=n))
    results = list(it.product(permutations, prefixes))
    enumerations = []
    for product in results:
        numbers, signs = product
        for i, number in enumerate(numbers):
            sign = signs[i]
            number = int(sign + str(number))
            enumerations.append(number)
    return enumerations


if __name__ == '__main__':
    d = 5

    if len(sys.argv) >= 2:
        d = int(utils.read_file_lines(sys.argv)[0])

    gene_orders = enumerate_oriented_gene_orders(d)
    print(int(len(gene_orders) / d))
    iterator = iter(gene_orders)
    for x in iterator:
        result = []
        result.append(x)
        for i in range(d - 1):
            result.append(next(iterator))
        print(' '.join(map(str, result)))
