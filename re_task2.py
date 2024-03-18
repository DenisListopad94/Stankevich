'''2)	Выведите строки, содержащие две буквы "z", между которыми ровно три символа.'''
import re

def find_strings_with_zz(string):
    matches = re.findall(r'z...z', string)
    return matches

input_string = "sdfkzzsfsz drgergzxddz zfsdfz zz wefw"
strings_with_zz = find_strings_with_zz(input_string)
print(strings_with_zz)