text = input("Введите строку: ")

#9 Дана строка. Необходимо проверить образуют ли строчные символы латиницы палиндром.
def is_palindrome(s):
    s = ''.join([c.lower() for c in s if c.isalpha()])
    return s == s[::-1]
if is_palindrome(text):
    print("Палиндром.")
else:
    print("НЕ палиндром.")