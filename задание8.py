#18 Дана строка. Необходимо найти наибольшее количество идущих подряд цифр.
import re
text = input("Введите строку: ")
digits_sequences = re.findall(r'\d+', text)

max_sequence = ""
max_length = 0

for sequence in digits_sequences:
    if len(sequence) > max_length:
        max_length = len(sequence)
        max_sequence = sequence

if max_sequence:
    print("Наибольшее количество идущих подряд цифр:", max_length," Последовательность:", max_sequence)
else:
    print("Цифр нет.")