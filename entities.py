# For installation of Spacy on your system please refer: https://spacy.io/usage 
# Reference: https://spacy.io/usage/linguistic-features

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("We sell fruits like Mango, Apple, Banana, etc. Our shop is in California.")

print([ent for ent in doc.ents])
# [Mango, Apple, California]
