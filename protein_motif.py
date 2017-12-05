import sys
import re
import urllib.request
import dna.utils as utils


def get_uniprot_fasta(uniprot_id):
    """get_uniprot_fasta(uniprot_id) - makes a network GET request to the uniprot server using an id which returns a fasta file.  This data is decoded into a 'utf-8' string."""
    data = ''
    with urllib.request.urlopen('http://www.uniprot.org/uniprot/{}.fasta'.format(uniprot_id)) as response:
        data = response.read().decode('utf-8')
    return data


def find_locations(id):
    """find_locations(id) - fetches the fasta of a protein id, then parses the fasta and looks for the locations of the protein motifs. returns an array of indcies, could be empty"""
    fasta = utils.parse_fasta(get_uniprot_fasta(id))
    pattern = r'(?=(N[^P][ST][^P]))'
    locations = []
    for match in re.finditer(pattern, str(fasta[0])):
        locations.append(match.start(0) + 1)
    return locations


if __name__ == '__main__':
    dataset = ['A2Z669', 'B5ZC00', 'P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST']
    if len(sys.argv) >= 2:
        dataset = utils.read_file_lines(sys.argv[1])

    # for each id, in the dataset, we figure out the locations from the remote fasta
    # and print out the id followed by the locations if they exist
    for access_id in dataset:
        if access_id.strip() is not '':
            locations = find_locations(access_id.strip())
            if len(locations):
                print(access_id.strip())
                print(' '.join(map(str, locations)))
