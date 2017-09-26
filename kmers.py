import sys


def kmer(k, t):
    k_mers = {}
    for i in range(0, len(t) + 1 - k):
        value = t[i:i + k].strip()
        if len(value) == k:
            k_mers[i] = value
    return k_mers


def read_file(filename):
    data = ""
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


if __name__ == '__main__':
    k = 5
    text = "CAATCCAAC"
    if len(sys.argv) >= 2:
        k, text = read_file(sys.argv[1])

    with open('output/answer_11.txt', 'w') as answer:
        print(*kmer(int(k), text).values(), sep='\n', end='\n', file=answer)
        print('Output written to %s' % answer.name)

    # expected = read_file('output/expected_11.txt')
    # output = read_file('output/answer_11.txt')
    # print("Lengths are equal:")
    # print(len(expected) == len(output))
    # has_all = True
    # for k in expected:
    # 	if not k in output:
    # 		has_all = False
    # 		break
    # print("Elements are in output")
    # print(has_all)
