'''6)	В каждой строке замените все вхождения подстроки "human" на подстроку "computer"
и выведите полученные строки.'''
import re

def replace_human_with_computer(string):
    replaced_string = re.sub(r'human', 'computer', string)
    return replaced_string

input_string = """Humans are intelligent creatures.
I am a human, but my friend is also a human.
There are many books written by humans."""
replaced_string = replace_human_with_computer(input_string)
print(replaced_string)