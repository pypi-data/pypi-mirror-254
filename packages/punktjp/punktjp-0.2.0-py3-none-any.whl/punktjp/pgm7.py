def print_prog():
    print(
        """
import re
from num2words import num2words


def replace_numbers(text):
    numbers = re.findall(r"\d+", text)
    for number in numbers:
        num = int(number)
        if num % 2 == 0:
            text = re.sub(r"\b" + number + r"\b", num2words(num), text)
        else:
            text = re.sub(r"\b" + number + r"\b", "", text)
    return text


with open("input.txt", "r") as file:
    text = file.read()

with open("output.txt", "w") as file:
    file.write(replace_numbers(text))

"""
    )
