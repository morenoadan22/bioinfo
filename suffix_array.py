import sys
import dna.utils as utils


def suffix_array(text):
    return [str(j[1]) for j in sorted([((s[i:], i)) for i in range(len(text))])]


if __name__ == '__main__':
    s = 'AACGATAGCGGTAGA$'
    if len(sys.argv) >= 2:
        s = utils.read_file_lines(sys.argv[1])[0].strip()

    print(', '.join(suffix_array(s)))

    with open('output/answer_21.txt', 'w') as out:
        print(', '.join(map(str, suffix_array(s))), file=out)
        print('Written to {}'.format(out.name))

    expected = utils.read_file('output/expected_suff_arr.txt')

    actual = utils.read_file('output/answer_21.txt')

    print(actual == expected)
