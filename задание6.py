#1 Дана строка. Необходимо найти максимальное из имеющихся в ней вещественных чисел.
import re
text = input("Введите строку: ")
numbers = re.findall(r'\d+\.\d+', text)

if numbers:
    max_number = max(map(float, numbers))
    print("Максимальное число в строке:", max_number)
else:
    print("Вещественных чисел нет.")
