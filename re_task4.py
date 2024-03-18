'''4)	Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.'''
import re

def find_words_starting_with_vowel(string):
    matches = re.findall(r'\b[aeiouAEIOU]\w*', string)
    return matches

input_string = "agregerg greerg erg"
vowel_words = find_words_starting_with_vowel(input_string)
print(vowel_words)