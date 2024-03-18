'''8)	Найти все слова, в которых есть хотя бы одна буква ‘b’'''
import re

def find_words_with_b(string):
    words = re.findall(r'\b\w*b\w*\b', string)
    return words

input_string = "wefwaebawha 44 tre vbervb reaghv ererg q4aehvregrnvb"
words_with_b = find_words_with_b(input_string)
print(words_with_b)