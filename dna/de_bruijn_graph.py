class DeBruijnGraph:
    """DeBruijnGraph
    A class that contains the data structure for building de Bruijn graphs from kmers
    """

    nodes = None
    current_node = None

    def append(self, node):
        self.nodes[node] += 1

    def __init__(self):
        self.nodes = {}

    def __str__(self):
        return '{0}'.format(self.nodes.keys())

    def __iter__(self):
        '__iter__() - return iterator'
        self.index = 0
        return self

    def __next__(self):
        'next() - next Node object'
        try:
            result = self.nodes.keys[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result
