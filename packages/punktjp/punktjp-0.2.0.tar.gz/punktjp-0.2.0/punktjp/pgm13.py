def print_prog():
    print(
        """
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

synm=[]

for syn in wordnet.synsets('happy'):
    for lemma in syn.lemmas():
        synm.append(lemma.name())

print(synm)
"""
    )
