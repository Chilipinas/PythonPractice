#2.	Написать функцию, которая принимает два аргумента: лямбда функция для фильтрации массива, массив строк. Сделать вызов данной функции для следующих функций фильтрации:
#•	Исключить строки с пробелами
#•	Исключить строки, начинающиеся с буквы “a”
#•	Исключить строки, длина которых меньше 5

def filter_strings(filter_func, string_list):
    return list(filter(filter_func, string_list))

string_list = ["привет мир", "апельсин", "яблоко", "банан", "кошка", "собака", "слон", "рыба"]
# Исключить строки с пробелами
no_spaces = lambda s: " " not in s
print(filter_strings(no_spaces, string_list))

# Исключить строки, начинающиеся с буквы “a”
no_a = lambda s: not s.startswith("а")
print(filter_strings(no_a, string_list))

# Исключить строки, длина которых меньше 5
long_enough = lambda s: len(s) >= 5
print(filter_strings(long_enough, string_list))