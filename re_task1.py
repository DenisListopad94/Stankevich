'''1)	Вам дана строка.
Выведите все подстроки, содержащие "cat".
'''

import re

def find_cat_substrings(string):
    matches = re.findall(r'cat', string)
    return matches

input_string = "cat eprgkopcat sefcat caawert fweca."
cat_substrings = find_cat_substrings(input_string)
print(cat_substrings)