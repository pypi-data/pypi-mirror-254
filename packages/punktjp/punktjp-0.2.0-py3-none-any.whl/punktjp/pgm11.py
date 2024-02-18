def print_prog():
    print(
        """
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities_and_relations(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    relations = [(chunk.text, chunk.root.head.text, " ".join(child.text for child in chunk.root.head.children if child.dep_ == "dobj")) for chunk in doc.noun_chunks if chunk.root.dep_ == "nsubj" and chunk.root.head.dep_ == "ROOT" and any(child.dep_ == "dobj" for child in chunk.root.head.children)]
    return entities, relations

sample_text = ''' jyothika from artificial intelligence and data science studying in final year at siddaganga institute of technology and she  loves to play sports and travelling and they are my friends and she  have a very good relation with my parents'''

entities, relations = extract_entities_and_relations(sample_text)
print("Entities:", entities)
print("Relations:", relations)

"""
    )
