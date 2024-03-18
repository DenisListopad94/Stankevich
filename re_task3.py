'''3)	Номер должен быть длиной 10 знаков и начинаться с 8 или 9.
Есть список телефонных номеров, и нужно проверить их, используя регулярные выражения в Python'''
import re

def check_phone_numbers(phone_numbers):
    valid_numbers = []
    for number in phone_numbers:
        # Проверяем номер на соответствие условиям: начинается с 8 или 9 и имеет длину 10 символов
        if re.match(r'^[89]\d{9}$', number):
            valid_numbers.append(number)
    return valid_numbers

# Пример списка телефонных номеров
phone_numbers = ['8912345678', '9123456789', '1234567890', '81234567890', '912345678']

valid_numbers = check_phone_numbers(phone_numbers)
print("Список действительных номеров:", valid_numbers)