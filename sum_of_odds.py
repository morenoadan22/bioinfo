import sys
import dna.utils as utils


def sum_of_odds(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 1:
            total += num
    return total


if __name__ == '__main__':
    start = 100
    end = 200

    if len(sys.argv) >= 2:
        file = utils.read_file_lines(sys.argv[1])
        start = int(file[0].split()[0])
        end = int(file[0].split()[1])

    print(sum_of_odds(start, end))
