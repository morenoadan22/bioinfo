def read_fasta(filename):
    data = read_file(filename)
    return parse_fasta(data)


def parse_fasta(target):
    data = []
    current_data = None
    for line in [l.strip() for l in target.splitlines()]:
        if line.startswith('>'):
            if current_data != None:
                data.append(current_data)
            current_data = ''
        else:
            current_data += line
    data.append(current_data)
    return data


def read_file(filename):
    data = ""
    with open(filename, 'r') as file:
        data = file.read()
    return data


def read_file_lines(filename):
    data = ''
    with open(filename, 'r') as file:
        data = file.readlines()
    return data
