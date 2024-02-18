def print_prog():
    print(
        """
import nltk

cfg = '''
S -> VP
VP -> V NP
NP -> Det N
N -> 'door'
Det -> 'the'
V -> 'open'
'''
parser = nltk.ChartParser(nltk.CFG.fromstring(cfg))
sent = "open the door"
words = sent.split()
for tree in parser.parse(words):
    tree.pretty_print()
"""
    )
