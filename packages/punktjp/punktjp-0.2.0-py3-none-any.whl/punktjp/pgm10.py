def print_prog():
    print(
        """
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract(text, query):
    tagged_words = nltk.pos_tag(nltk.word_tokenize(text))
    return [word for word, pos in tagged_words if pos in query]

file_path, search_query = 'pgm10input.txt', ['VB', 'NN', 'NNS']
with open(file_path, 'r', encoding='utf-8') as file:
    print(extract(file.read(), search_query))
"""
    )
