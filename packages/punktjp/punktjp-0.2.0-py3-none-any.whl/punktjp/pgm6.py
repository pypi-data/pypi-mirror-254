def print_prog():
    print(
        """
import re
from bs4 import BeautifulSoup
from spellchecker import SpellChecker

spell = SpellChecker()
with open("input.txt", "r") as f:
    input = f.read()
text = BeautifulSoup(input, "html.parser").get_text()
text = re.sub(r"http[s]?//\S+", "", text)
text = " ".join(text.split())
corrected = [spell.correction(word) for word in text.split()]
corrected = [correct for correct in corrected if correct]
with open("output.txt", "w") as f:
    f.write(" ".join(corrected))

"""
    )
