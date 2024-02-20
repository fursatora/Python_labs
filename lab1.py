#задание2 вар1
text = input("Введите строку: ")


#1 Дана строка. Необходимо найти общее количество русских символов.
def count_russian_characters(text):
        russian_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        russian_chars += russian_chars.upper()

        count = 0
        for char in text:
            if char in russian_chars:
                count += 1
        return count
print("Количество русских символов в тексте:", count_russian_characters(text))


#9 Дана строка. Необходимо проверить образуют ли строчные символы латиницы палиндром.
def is_palindrome(s):
    s = ''.join([c.lower() for c in s if c.isalpha()])
    return s == s[::-1]
if is_palindrome(text):
    print("Палиндром.")
else:
    print("НЕ палиндром.")


#18 Найти в тексте даты формата «день.месяц.год».
import re
def find_dates(text):
    pattern = r'\b(\d{1,2}\.\d{1,2}\.\d{4})\b'
    dates = re.findall(pattern, text)
    return dates

if find_dates(text):
    for date in find_dates(text):
        print(date)
else:
    print("Формата «день.месяц.год» НЕТ.")




