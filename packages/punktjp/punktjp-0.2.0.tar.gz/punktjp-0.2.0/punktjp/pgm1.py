def print_prog():
    print(
        """
import re

fileslist = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]

for file in fileslist:
    with open(file, "w") as f:
        print("Enter 5 sentences:")

        for i in range(5):
            data = input()

            f.write(data + "\n")

pattern = input("Enter search pattern")

results = []


def highlight(match):
    return f"\033[91;1m{match.group()}\033[0m"


for file in fileslist:
    with open(file, "r") as f:
        sentences = f.readlines()

        for i, sentence in enumerate(sentences):
            modified_sentence = re.sub(pattern, highlight, sentence)

            if modified_sentence != sentence:
                result = {
                    "file": file,
                    "sentence": modified_sentence.strip(),
                }

                results.append(result)

for result in results:
    print(f'Pattern found in file {result["file"]}:')
    print(f'Sentence: {result["sentence"]}')

"""
    )
