class Node:
	""" Node
	A class that holds a kmer section of dna
	"""

	kmer = None
	edges = None


	def add_edge(self, edge):
		self.edges.append(edge)

	def __init__(self, kmer):
		self.kmer = kmer
		self.edges = set()


	def __str__(self):
		return self.kmer


