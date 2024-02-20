#9 Дана строка. Необходимо найти минимальное из имеющихся в ней рациональных чисел.
import re
text = input("Введите строку: ")
numbers = re.findall(r' -?\d+ ', text)

if numbers:
    numbers = list(map(float, numbers))
    min_number = min(numbers)
    print("Минимальное :", min_number)
else:
    print("Чисел нет.")

