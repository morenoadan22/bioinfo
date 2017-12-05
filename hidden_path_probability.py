import sys
import dna.utils as utils
import numpy as np


def path_probability(path, matrix):
    print(path)
    print(matrix)
    product = 0.5  # probability of the first letter being A or B
    for i, k in zip(path[0::1], path[1::1]):
        if i == 'A' and k == 'A':
            product *= matrix.item(0)
        elif i == 'A' and k == 'B':
            product *= matrix.item(1)
        elif i == 'B' and k == 'A':
            product *= matrix.item(2)
        elif i == 'B' and k == 'B':
            product *= matrix.item(3)

    return product


if __name__ == '__main__':
    path = 'AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB'
    transition_matrix = np.matrix([[0.194, 0.806], [0.273, 0.727]])

    # read the dataset file in and construct the numpy matrix and path
    if len(sys.argv) >= 2:
        file_lines = utils.read_file_lines(sys.argv[1])
        path = file_lines[0]
        last_line = np.array(file_lines[len(file_lines) - 1].split()[1:])
        second_to_last = np.array(file_lines[len(file_lines) - 2].split()[1:])
        transition_matrix = np.column_stack((second_to_last.astype(float), last_line.astype(float)))

    print(format(path_probability(path, transition_matrix), '.11e'))
