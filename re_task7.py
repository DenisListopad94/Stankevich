'''7)	Извлечь дату из строки. Формат даты dd –mm-yyyy (например, 2022-02-28).'''
import re

def extract_date(string):
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'  # Регулярное выражение для даты в формате "dd-mm-yyyy"
    match = re.search(pattern, string)
    if match:
        return match.group()
    else:
        return "Дата не найдена"

input_string = "12-05-2005"
date = extract_date(input_string)
print(date)