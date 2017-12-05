import sys
import dna.utils as utils
import numpy as np


def path_probability(initial, result, matrix):
    if initial == 'x' and result == 'A':
        item_number = 0
    elif initial == 'y' and result == 'A':
        item_number = 1
    elif initial == 'z' and result == 'A':
        item_number = 2
    elif initial == 'x' and result == 'B':
        item_number = 3
    elif initial == 'y' and result == 'B':
        item_number = 4
    elif initial == 'z' and result == 'B':
        item_number = 5
    else:
        print('none')
        return 1

    return matrix.item(item_number)


def calculate_probability(x, emission, transition_matrix):
    product = 1
    for (i, o) in zip(x, emission):
        product *= path_probability(i, o, transition_matrix)
    return product


if __name__ == '__main__':
    x = 'xxyzyxzzxzxyxyyzxxzzxxyyxxyxyzzxxyzyzxzxxyxyyzxxzx'
    emission = 'BBBAAABABABBBBBBAAAAAABAAAABABABBBBBABAABABABABBBB'

    transition_matrix = np.matrix([[0.612, 0.314, 0.074], [0.346, 0.317, 0.336]])

    # read the dataset file in and construct the numpy matrix and path
    if len(sys.argv) >= 2:
        file_lines = utils.read_file_lines(sys.argv[1])
        x = file_lines[0]
        emission = file_lines[4]
        second_row = np.array(file_lines[len(file_lines) - 1].split()[1:]).astype(float)
        first_row = np.array(file_lines[len(file_lines) - 2].split()[1:]).astype(float)
        transition_matrix = np.array([first_row, second_row])
        print(transition_matrix)
        for i in range(6):
            print(transition_matrix.item(i))

    print(format(calculate_probability(x, emission, transition_matrix), '.11e'))
