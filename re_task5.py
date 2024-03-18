'''5)	Дана строка. Вывести все числа этой строки, как отрицательные так и положительные. '''
import re

def find_numbers(string):
    matches = re.findall(r'-?\d+', string)
    return matches

input_string = "sef1000 esfsef5 esf gger 5632 -7898 0 -3"
numbers = find_numbers(input_string)
print(numbers)